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
