class Person:
    age = 20
    __college = "Trinity"

    @classmethod
    def get_college(cls):
        return cls.__college
    
    @staticmethod
    def get_info():
        return "i am learning python"
    

    @classmethod
    def set_college(cls, college):
        cls.__college = college


Person.__colle = 40
print(Person.__college)
print(Person.age)  # 20

p = Person()
p.__college = "CCRC"
print(p.__college)
print(Person.__college)

print(Person.get_college())
Person.set_college("ITCOllege")
print(Person.get_college())

print(p.get_info)