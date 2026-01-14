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

from collections import defaultdict

from app.building.floorcategory import FloorCategory


class Building:
    def __init__(self, floor_definition):
        self.floor_definition = floor_definition
        self.number_of_floors = len(floor_definition.items())
        self.floors_per_category = self.get_floors_per_category()

        assert self.floors_per_category[FloorCategory.ENTRANCE]

    def get_floors_per_category(self):
        floors_per_category = defaultdict(list)
        for floor_number, category in self.floor_definition.items():
            floors_per_category[category].append(floor_number)
        return dict(floors_per_category)

    def get_floors_for_category(self, category):
        return self.floors_per_category.get(category, [])

    def get_entrance_floors(self):
        return self.floors_per_category.get(FloorCategory.ENTRANCE, [])
