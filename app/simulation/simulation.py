import threading
import uuid
from hashlib import sha256
from flask import Flask, jsonify, request, Response, render_template_string
from app.building.building import Building
from app.building.floordefinition import FLOOR_DEFINITION
from app.elevator.elevator import Elevator
from app.elevator.scheduling.elevator_scheduler import Scheduler
from app.statistics.ride_log import RideLog
from app.statistics.statistics import Statistics
from app.people.population import Population
from app.people.roledistribution import ROLE_DISTRIBUTION
from app.simulation.loop import Loop
from app.simulation.virtual_clock import VirtualClock

# Constants
POPULATION_SIZE = 100
MAX_LOAD = 1200

# Initialize Flask app
app = Flask(__name__)

building = Building(FLOOR_DEFINITION)
population = Population(POPULATION_SIZE, building, ROLE_DISTRIBUTION)
elevator = Elevator(building.number_of_floors, MAX_LOAD)
scheduler = Scheduler(elevator)
clock = VirtualClock(scale=120)
statistics = Statistics(clock)
ride_log = RideLog(clock)
loop = Loop(scheduler, elevator, population, clock, statistics, ride_log, iteration_interval=0.125, stop_time=0.25)


@app.route('/elevator/stream', methods=['GET'])
def stream_elevator():
    """ Streams the elevator state in real-time. """
    return Response(loop.generate_ascii_art(), mimetype='text/event-stream')


@app.route('/elevator')
def index():
    """ Serves a simple webpage to display elevator status."""
    return render_template_string('''
        <!DOCTYPE html>
<html>
<head>
    <title>Elevator Monitor</title>
    <style>
        body { font-family: monospace; white-space: pre-wrap; }
        pre { font-size: 16px; }
    </style>
</head>
<body>
    <h1>Realtime Elevator View</h1>
    <pre id="output">Connecting...</pre>
    <script>
        const output = document.getElementById("output");
        const eventSource = new EventSource("/elevator/stream");

        eventSource.onmessage = function(event) {
            output.textContent = event.data;  // Use textContent to preserve formatting
        };

        eventSource.onerror = function() {
            output.textContent = "Connection lost. Trying to reconnect...";
        };
    </script>
</body>
</html>
    ''')


@app.route('/elevator/current_time', methods=['GET'])
def get_current_time():
    """ Returns the current time of the virtual clock."""
    return jsonify(str(clock))


@app.route('/elevator/cabin_state', methods=['GET'])
def get_elevator_state():
    """ Returns the current state of the elevator."""
    return jsonify(elevator.get_state())


@app.route('/elevator/scheduler_state', methods=['GET'])
def get_scheduler_state():
    """ Returns the current state of the scheduler."""
    return jsonify(scheduler.get_state())


@app.route('/elevator/statistics', methods=['GET'])
def get_stats():
    """ Returns the current statistics of the elevator."""
    return jsonify(statistics.get())


@app.route('/elevator/log', methods=['GET'])
def get_log():
    """ Returns the current statistics of the elevator."""
    return jsonify(ride_log.get())


@app.route('/elevator/population', methods=['GET'])
def get_population():
    """ Returns the current statistics of the elevator."""
    return jsonify(population.get_population())


@app.route('/elevator/request_ride', methods=['GET'])
def request_ride():
    """ Handles ride requests with start and end floors."""
    start = request.args.get('start', type=int)
    end = request.args.get('end', type=int)

    if start is None or end is None:
        return jsonify({'error': 'Missing start or end floor'}), 400

    if not (0 <= start < building.number_of_floors and 0 <= end < building.number_of_floors):
        return jsonify({'error': 'Invalid floor range'}), 400

    scheduler.handle_request(start, end)
    statistics.track_ride(start, end)

    response = jsonify({'message': 'Ride requested successfully'})

    user_id = request.cookies.get("user_id")
    if not user_id:
        user_id = str(uuid.uuid4())
        response.set_cookie("user_id", user_id, max_age=60 * 60 * 24 * 365)

    person_id = sha256(user_id.encode("utf-8")).hexdigest()
    ride_log.log_ride(start, end, person_id)
    return response


if __name__ == "__main__":
    loop_thread = threading.Thread(target=loop.run, daemon=True)
    loop_thread.start()
    app.run(host='0.0.0.0', port=5000, debug=True)
