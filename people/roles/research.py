from building.floorcategory import FloorCategory
from people.roles.baserole import BaseRole

SCHEDULE = [
    (9, 12, [
        FloorCategory.MEETING,
        FloorCategory.EXECUTIVE_OFFICES,
        FloorCategory.ENGINEERING
    ]),
    (12, 14, [FloorCategory.RECREATION]),
    (14, 16, [
        FloorCategory.EXECUTIVE_OFFICES,
        FloorCategory.ENGINEERING,
    ]),
    (16, 19, [FloorCategory.ENGINEERING])
]


class ResearchRole(BaseRole):
    def __init__(self, building):
        super().__init__(
            building,
            SCHEDULE,
            punctuality=0,
            punctuality_variance=60,
            lingering=90,
            overtime=30,
            overtime_variance=240
        )
