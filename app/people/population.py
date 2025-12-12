import random
from typing import List

from app.people.person import Person


class Population:
    def __init__(self, population_size, building, role_distribution):
        self.role_distribution = role_distribution
        self.building = building
        self.population_size = population_size
        self.role_distribution = role_distribution
        self.population = self.init_population()

    def init_population(self):
        """Initializes the population with role objects instantiated according to the defined distribution."""
        population = []
        role_classes = list(self.role_distribution.keys())  # Extract role class references
        probabilities = list(self.role_distribution.values())  # Corresponding probabilities

        for _ in range(self.population_size):
            assigned_role_class = random.choices(role_classes, weights=probabilities, k=1)[0]
            population.append(Person(assigned_role_class(self.building)))

        return population

    def get_people(self) -> List[Person]:
        return self.population

    def get_population(self):
        population_summary = {role.__name__: 0 for role in self.role_distribution.keys()}
        for person in self.population:
            population_summary[person.role.__class__.__name__] += 1
        return population_summary
