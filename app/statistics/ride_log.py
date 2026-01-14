# Copyright 2026 Tobias Hafner
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from collections import deque
from datetime import datetime


class RideLog:
    def __init__(self, clock, size=1000):
        """
        Initializes the RideLog object to track the last 1000 rides.
        :param clock: An optional clock object with a getter method returning the current time.
        """
        self.clock = clock
        self.rides = deque(maxlen=size)

    def log_ride(self, start, end, person_id=None, role=None):
        """
        Logs a ride with timestamps and API request data if available.
        :param start: The departure floor
        :param end: The destination floor
        :param id: Unique id of the user requesting the ride
        """
        ride_entry = {
            "virtual_time": self.clock.get_virtual_seconds_since_epoch(),
            "real_time": int(datetime.now().timestamp()),
            "start": start,
            "end": end,
            "person_id": person_id,
            "role": role
        }
        self.rides.append(ride_entry)

    def get(self):
        """
        Returns the last 1000 rides as a list of dictionaries.
        """
        return list(self.rides)

