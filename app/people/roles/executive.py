from app.building.floorcategory import FloorCategory
from app.people.roles.baserole import BaseRole

SCHEDULE = [
    (9, 12, [FloorCategory.MEETING, FloorCategory.EXECUTIVE_OFFICES]),
    (12, 13, [FloorCategory.RECREATION]),
    (13, 16, [FloorCategory.OFFICES, FloorCategory.EXECUTIVE_OFFICES])
]


class ExecutiveRole(BaseRole):
    def __init__(self, building):
        super().__init__(
            building,
            SCHEDULE,
            punctuality=0,
            punctuality_variance=60,
            lingering=90,
            overtime=0,
            overtime_variance=30
        )
