import random

import numpy as np


class BaseRole:
    def __init__(
            self, building, schedule,
            punctuality=0, punctuality_variance=2,
            lingering=0.7,
            overtime=0, overtime_variance=15,
            start_floor=0
    ):
        self.building = building
        self.schedule = schedule
        self.punctuality = punctuality
        self.punctuality_variance = punctuality_variance
        self.lingering = lingering
        self.overtime = overtime
        self.overtime_variance = overtime_variance
        self.current_floor = start_floor
        self.next_move = self.get_next_move(0)
        self.overtime_end = None

    def get_next_move(self, current_time):
        return current_time + np.random.normal(self.lingering, self.lingering)

    def get_next_request(self, clock):
        """
        Determines the next floor request based on schedule and role traits.
        """
        current_time_minutes = clock.get_virtual_minutes()

        if current_time_minutes < self.next_move:
            return None

        for start_hour, end_hour, categories in self.schedule:
            start_minutes = start_hour * 60
            end_minutes = end_hour * 60

            # Use Gaussian distribution for punctuality: mean = punctuality, std deviation = punctuality_variance
            punctuality_offset = int(np.random.normal(self.punctuality, self.punctuality_variance))
            adjusted_start = start_minutes + punctuality_offset
            adjusted_end = end_minutes + punctuality_offset

            if not adjusted_start <= current_time_minutes < adjusted_end:
                continue

            # Pick a new floor if lingering is low or no previous floor set
            random_category = random.choice(categories)
            random_floor = random.choice(self.building.get_floors_for_category(random_category))
            if self.current_floor == random_floor:
                return None

            self.next_move = self.get_next_move(current_time_minutes)

            old_floor = self.current_floor
            self.current_floor = random_floor
            return old_floor, random_floor

        # Handle overtime behavior if no interval matches
        if self.overtime_end is None:
            # Use Gaussian distribution for overtime: mean = overtime, std deviation = overtime_variance
            overtime_offset = int(np.random.normal(self.overtime, self.overtime_variance))
            self.overtime_end = current_time_minutes + overtime_offset

        if current_time_minutes < self.overtime_end:
            return None  # Keep staying before finally leaving

        self.overtime_end = None

        # When overtime ends, move to the entrance
        if self.current_floor == 0:
            return None

        self.next_move = self.get_next_move(current_time_minutes)

        old_floor = self.current_floor
        self.current_floor = random.choice(self.building.get_entrance_floors())
        return old_floor, self.current_floor,
