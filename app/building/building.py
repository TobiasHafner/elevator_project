from collections import defaultdict

from app.building.floorcategory import FloorCategory


class Building:
    def __init__(self, floor_definition):
        self.floor_definition = floor_definition
        self.number_of_floors = len(floor_definition.items())
        self.floors_per_category = self.get_floors_per_category()

        assert self.floors_per_category[FloorCategory.ENTRANCE]

    def get_floors_per_category(self):
        floors_per_category = defaultdict(list)
        for floor_number, category in self.floor_definition.items():
            floors_per_category[category].append(floor_number)
        return dict(floors_per_category)

    def get_floors_for_category(self, category):
        return self.floors_per_category.get(category, [])

    def get_entrance_floors(self):
        return self.floors_per_category.get(FloorCategory.ENTRANCE, [])
