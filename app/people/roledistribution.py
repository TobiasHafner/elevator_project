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

from app.people.roles.cleaning import CleaningRole
from app.people.roles.executive import ExecutiveRole
from app.people.roles.maintenance import MaintenanceRole
from app.people.roles.office import OfficeRole
from app.people.roles.research import ResearchRole
from app.people.roles.security import SecurityRole
from app.people.roles.storage import StorageRole

ROLE_DISTRIBUTION = {
    CleaningRole: 10,
    ExecutiveRole: 5,
    MaintenanceRole: 10,
    OfficeRole: 40,
    ResearchRole: 20,
    SecurityRole: 5,
    StorageRole: 10
}
