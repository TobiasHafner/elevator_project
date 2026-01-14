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

FLOOR_DEFINITION = {
    0: FloorCategory.ENTRANCE,
    1: FloorCategory.STORAGE,
    2: FloorCategory.OFFICES,
    3: FloorCategory.OFFICES,
    4: FloorCategory.MEETING,
    5: FloorCategory.OFFICES,
    6: FloorCategory.MEETING,
    7: FloorCategory.OFFICES,
    8: FloorCategory.MEETING,
    9: FloorCategory.OFFICES,
    10: FloorCategory.OFFICES,
    11: FloorCategory.MAINTENANCE,
    12: FloorCategory.ENGINEERING,
    13: FloorCategory.ENGINEERING,
    14: FloorCategory.ENGINEERING,
    15: FloorCategory.EXECUTIVE_OFFICES,
    16: FloorCategory.RECREATION,
}
