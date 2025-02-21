import time

from elevator.scheduling.scheduler_moves import Moves


class Loop:
    def __init__(self, scheduler, elevator, population, clock, statistics, logger, iteration_interval=0.5, stop_time=1):
        self.scheduler = scheduler
        self.elevator = elevator
        self.population = population
        self.clock = clock
        self.statistics = statistics
        self.logger = logger
        self.iteration_interval = iteration_interval
        self.stop_time = stop_time

    def run(self):
        while True:
            for person in self.population.get_people():
                request = person.get_next_request(self.clock)
                if request is None:
                    continue
                start, end = request
                self.scheduler.handle_request(start, end)
                self.statistics.track_ride(start, end)
                self.logger.log_ride(start, end, person.get_employee_id(), person.role.__class__.__name__)

                # Process elevator moves
            move = self.scheduler.get_next_move()
            match move:
                case Moves.UP:
                    self.elevator.close_doors()
                    self.elevator.move_up()
                case Moves.STOP:
                    self.elevator.open_doors()
                case Moves.DOWN:
                    self.elevator.close_doors()
                    self.elevator.move_down()
                case Moves.STAY:
                    self.elevator.close_doors()

            if self.elevator.get_door_state():
                time.sleep(self.stop_time)
            time.sleep(self.iteration_interval)

    def generate_ascii_art(self):
        while True:
            elevator_status = str(self.elevator)
            scheduler_status = str(self.scheduler)
            current_time = f"Current Time: {str(self.clock)}"
            ascii_output = f"{current_time}\n\n{elevator_status}\n{scheduler_status}"
            formatted_data = "\n".join([f"data: {line}" for line in ascii_output.split("\n")])
            yield f"{formatted_data}\n\n"
            time.sleep(self.iteration_interval)
