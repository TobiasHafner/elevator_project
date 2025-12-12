from app.building.floorcategory import FloorCategory
from app.people.roles.baserole import BaseRole

SCHEDULE = [
    (9, 13, [
        FloorCategory.MAINTENANCE,
        FloorCategory.OFFICES,
        FloorCategory.STORAGE,
        FloorCategory.EXECUTIVE_OFFICES,
        FloorCategory.ENGINEERING,
    ]),
    (13, 14, [FloorCategory.RECREATION]),
    (13, 17, [
        FloorCategory.MAINTENANCE,
        FloorCategory.OFFICES,
        FloorCategory.STORAGE,
        FloorCategory.EXECUTIVE_OFFICES,
        FloorCategory.ENGINEERING,
    ])
]


class MaintenanceRole(BaseRole):
    def __init__(self, building):
        super().__init__(
            building,
            SCHEDULE,
            punctuality=5,
            punctuality_variance=5,
            lingering=45,
            overtime=-5,
            overtime_variance=15
        )
