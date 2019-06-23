class Employee:
    def __init__(self, first_name: str, last_name: str, salary: int):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.salary = salary
        self.email = "{}_{}@example.com".format(first_name.lower(), last_name.lower())

    @property
    def full_name(self) -> str:
        return "{}, {}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, full_name: str) -> None:
        first_name, last_name = full_name.split(",")
        self.first_name = first_name.capitalize()
        self.last_name = last_name[1:len(last_name)].capitalize()

    @classmethod
    def from_str(cls, string: str):
        first_name, last_name, salary = string.split(",")
        return Employee(first_name, last_name, int(salary))


class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, salary: int, subordinates=[]):
        super().__init__(first_name, last_name, salary)
        self.subordinates = subordinates

    def add_subordinate(self, subordinate: Employee) -> None:
        if subordinate not in self.subordinates:
            self.subordinates.append(subordinate)

    def remove_subordinate(self, subordinate: Employee) -> None:
        if isinstance(subordinate, Employee) and (subordinate in self.subordinates):
            self.subordinates.remove(subordinate)
        elif isinstance(subordinate, str) and (subordinate in [employee.email for employee in self.subordinates]):
            self.subordinates.remove(self.find_using_email(subordinate))

    def find_using_email(self, email: str) -> Employee:
        for subordinate in self.subordinates:
            if subordinate.email == email:
                return subordinate


class DevOps(Employee):
    def __init__(self, first_name: str, last_name: str, salary: int, skills=[]):
        super().__init__(first_name, last_name, salary)
        self.skills = skills

    def add_skill(self, skill: str) -> None:
        skill = skill.lower().capitalize()
        if skill not in self.skills:
            self.skills.append(skill)

    def remove_skill(self, skill) -> None:
        skill = skill.lower().capitalize()
        if skill in self.skills:
            self.skills.remove(skill)
