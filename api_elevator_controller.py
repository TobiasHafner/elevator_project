import threading
import time

from flask import Flask, jsonify, request, Response

from elevator import Elevator
from elevator_scheduler import Scheduler
from request_generator import RequestGenerator
from scheduler_moves import Moves

# Constants
FLOOR_COUNT = 16
MAX_LOAD = 1200
ITERATION_INTERVAL = 2  # Time in seconds between iterations
REQUEST_PROBABILITY = 0.3  # Probability of generating a new request

# Initialize Flask app
app = Flask(__name__)

# Initialize Elevator and Scheduler
elevator = Elevator(FLOOR_COUNT, MAX_LOAD)
scheduler = Scheduler(elevator)
request_generator = RequestGenerator(FLOOR_COUNT, REQUEST_PROBABILITY)


def run_elevator():
    """ Runs the elevator continuously in a separate thread."""
    while True:
        # Generate random requests
        request = request_generator.generate_request()
        split = request.split()
        if len(split) != 0:
            start = int(split[0])
            end = int(split[1])
            scheduler.handle_request(start, end)

        # Process elevator moves
        move = scheduler.get_next_move()
        match move:
            case Moves.UP:
                elevator.close_doors()
                elevator.move_up()
            case Moves.STOP:
                elevator.open_doors()
            case Moves.DOWN:
                elevator.close_doors()
                elevator.move_down()
            case Moves.STAY:
                elevator.close_doors()

        time.sleep(ITERATION_INTERVAL)


@app.route('/elevator', methods=['GET'])
def get_elevator_ascii_art():
    """ Returns the current state of the elevator."""
    ascii_art = str(elevator)
    ascii_art += '\n'
    ascii_art += str(scheduler)
    return Response(ascii_art, mimetype="text/plain")


@app.route('/elevator/cabin_state', methods=['GET'])
def get_elevator_state():
    """ Returns the current state of the elevator."""
    return jsonify(elevator.get_state())


@app.route('/elevator/scheduler_state', methods=['GET'])
def get_scheduler_state():
    """ Returns the current state of the scheduler."""
    return jsonify(scheduler.get_state())


@app.route('/elevator/request_ride', methods=['GET'])
def request_ride():
    """ Handles ride requests with start and end floors."""
    start = request.args.get('start', type=int)
    end = request.args.get('end', type=int)

    if start is None or end is None:
        return jsonify({'error': 'Missing start or end floor'}), 400

    if not (0 <= start < FLOOR_COUNT and 0 <= end < FLOOR_COUNT):
        return jsonify({'error': 'Invalid floor range'}), 400

    scheduler.handle_request(start, end)
    return jsonify({'message': 'Ride requested successfully'})


if __name__ == "__main__":
    # Start the elevator loop in a separate thread
    elevator_thread = threading.Thread(target=run_elevator, daemon=True)
    elevator_thread.start()

    app.run(host='0.0.0.0', port=5000, debug=True)
