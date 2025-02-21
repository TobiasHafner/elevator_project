from building.floorcategory import FloorCategory
from people.roles.baserole import BaseRole

SCHEDULE = [
    (14, 15, [FloorCategory.RECREATION]),
    (18, 20, [
        FloorCategory.OFFICES,
        FloorCategory.MEETING,
        FloorCategory.ENGINEERING,
        FloorCategory.EXECUTIVE_OFFICES,
        FloorCategory.ENTRANCE,
        FloorCategory.STORAGE
    ])
]


class CleaningRole(BaseRole):
    def __init__(self, building):
        super().__init__(
            building,
            SCHEDULE,
            punctuality=-5,
            punctuality_variance=5,
            lingering=20,
            overtime=0,
            overtime_variance=2
        )
