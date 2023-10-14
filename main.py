import random


class Asshole:
    def __init__(self, type_asshole, sex, age, hands_count=2):
        print("i'm is", type_asshole + "!")
        print("i'm is", sex)
        self.say = "Гутен таг"
        self._hands_count = hands_count
        self.type_of_armor = "leather"
        self._age = age

    age = property()

    @property
    def hands(self):
        print("use property")
        return self._hands_count

    @age.setter
    def age(self, value):
        if value < 0:
            print("i'm koshey")
        else:
            print("test")
            self._age = value


    @age.getter
    def age(self):
        print("getting")
        return self._age

    @age.deleter
    def age(self):
        print("i'm dead")
        del self._age

    def status_available(self):
        return random.choice([True, False])


    def abilityes(self):
        return random.choice([True, False])


    def __del__(self):
        print("I'm die")

def main(name):
    # Use a breakpoint in the code line below to debug your script.
    slave = "slave"
    male = "male"

    # unit_1 = Asshole(slave, male)
    # unit_2 = Asshole("master", "male")
    unit_3 = Asshole("swordsman", "male", 10)

    # if unit_1.status_available():
    #     print("i'm available")
    #     print(unit_1.say)
    # else:
    #     print("i'm busy")
    #     unit_1.hands_count -= 1

    if unit_3.abilityes():
        print("i'm shooting")
    else:
        print("i'm kicking")
        print("i'm wear", unit_3.type_of_armor, "armor")

    unit_3.age = 10
    print(unit_3.age)
    del unit_3.age

    print("property")
    unit_3.hands
    print("--")

    # print("i have", unit_2.hands_count, "хандс штук")
    # print("i have", unit_1.hands_count, "хандс штук")
    #
    # del unit_1
    # print("ещё не конец")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')