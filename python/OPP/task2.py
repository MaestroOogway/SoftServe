class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return "HI", self.name

    @classmethod
    def get_species(cls):
        return f"It is a species of {cls.species}"

    @staticmethod
    def arbitrary_message():
        return "This is a static method message."
    
human1 = Human("fabian")
print(human1.say_hi())
print(Human.get_species())
print(Human.arbitrary_message())