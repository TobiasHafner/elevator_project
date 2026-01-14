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

from app.building.floorcategory import FloorCategory
from app.people.roles.baserole import BaseRole

SCHEDULE = [
    (9, 13, [
        FloorCategory.MAINTENANCE,
        FloorCategory.OFFICES,
        FloorCategory.STORAGE,
        FloorCategory.EXECUTIVE_OFFICES,
        FloorCategory.ENGINEERING,
    ]),
    (13, 14, [FloorCategory.RECREATION]),
    (13, 17, [
        FloorCategory.MAINTENANCE,
        FloorCategory.OFFICES,
        FloorCategory.STORAGE,
        FloorCategory.EXECUTIVE_OFFICES,
        FloorCategory.ENGINEERING,
    ])
]


class MaintenanceRole(BaseRole):
    def __init__(self, building):
        super().__init__(
            building,
            SCHEDULE,
            punctuality=5,
            punctuality_variance=5,
            lingering=45,
            overtime=-5,
            overtime_variance=15
        )
