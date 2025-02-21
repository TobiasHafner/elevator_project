from people.roles.cleaning import CleaningRole
from people.roles.executive import ExecutiveRole
from people.roles.maintenance import MaintenanceRole
from people.roles.office import OfficeRole
from people.roles.research import ResearchRole
from people.roles.security import SecurityRole
from people.roles.storage import StorageRole

ROLE_DISTRIBUTION = {
    CleaningRole: 10,
    ExecutiveRole: 5,
    MaintenanceRole: 10,
    OfficeRole: 40,
    ResearchRole: 20,
    SecurityRole: 5,
    StorageRole: 10
}
