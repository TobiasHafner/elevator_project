import uuid


class Person:
    def __init__(self, role):
        self.role = role
        self.employee_id = uuid.uuid4()

    def get_employee_id(self):
        return self.employee_id

    def get_next_request(self, clock):
        request = self.role.get_next_request(clock)
        return request
