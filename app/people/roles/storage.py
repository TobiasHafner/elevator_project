from app.building.floorcategory import FloorCategory
from app.people.roles.baserole import BaseRole

SCHEDULE = [
    (7, 12, [
        FloorCategory.ENTRANCE,
        FloorCategory.ENGINEERING,
        FloorCategory.STORAGE,
    ]),
    (12, 13, [FloorCategory.RECREATION]),
    (13, 16, [
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


class StorageRole(BaseRole):
    def __init__(self, building):
        super().__init__(
            building,
            SCHEDULE,
            punctuality=5,
            punctuality_variance=30,
            lingering=45,
            overtime=5,
            overtime_variance=10
        )
