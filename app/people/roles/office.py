from app.building.floorcategory import FloorCategory
from app.people.roles.baserole import BaseRole

SCHEDULE = [
    (8, 11, [
        FloorCategory.MEETING,
        FloorCategory.OFFICES,
    ]),
    (12, 13, [FloorCategory.RECREATION]),
    (13, 15, [
        FloorCategory.OFFICES,
        FloorCategory.EXECUTIVE_OFFICES,
        FloorCategory.ENGINEERING,
    ]),
    (16, 17, [FloorCategory.OFFICES])
]


class OfficeRole(BaseRole):
    def __init__(self, building):
        super().__init__(
            building,
            SCHEDULE,
            punctuality=0,
            punctuality_variance=20,
            lingering=60,
            overtime=0,
            overtime_variance=60
        )
