from building.floorcategory import FloorCategory
from people.roles.baserole import BaseRole

SCHEDULE = [
    (18, 24, [
        FloorCategory.ENTRANCE,
        FloorCategory.MEETING,
        FloorCategory.OFFICES,
        FloorCategory.ENGINEERING,
        FloorCategory.RECREATION,
        FloorCategory.STORAGE,
        FloorCategory.MAINTENANCE,
        FloorCategory.EXECUTIVE_OFFICES
    ]),
    (0, 6, [
        FloorCategory.ENTRANCE,
        FloorCategory.MEETING,
        FloorCategory.OFFICES,
        FloorCategory.ENGINEERING,
        FloorCategory.RECREATION,
        FloorCategory.STORAGE,
        FloorCategory.MAINTENANCE,
        FloorCategory.EXECUTIVE_OFFICES
    ]),
]


class SecurityRole(BaseRole):
    def __init__(self, building):
        super().__init__(
            building,
            SCHEDULE,
            punctuality=-5,
            punctuality_variance=5,
            lingering=30,
            overtime=0,
            overtime_variance=5
        )
