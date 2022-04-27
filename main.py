from random import randrange


class Tamagotchi(object):
    vocabulary = ["Hi!"]

    food_maximum = 100
    food_reduce = 10
    food_warning = 30

    happiness_maximum = 100
    happiness_reduce = 10
    happiness_warning = 30

    def __init__(self, animal_type, name):
        """Creates a virtual pet"""
        self.animal_type = animal_type
        self.name = name

        self.food = randrange(0, self.food_maximum)
        self.happiness = randrange(0, self.happiness_maximum)

        print("Hi! My name is " + name + ", I am new here!")

    def __state_change__(self):
        """Each action reduces parameters of food and happiness"""
        self.food -= self.food_reduce
        self.happiness -= self.happiness_reduce

        if self.food <= 0:
            self.food = 0
        if self.happiness <= 0:
            self.happiness = 0

    def learn_word(self, word):
        """Adds words to the vocabulary"""
        self.vocabulary.append(word)
        self.__state_change__()
        print("Got it!")

    @property
    def mood(self):
        if self.food > self.food_warning and self.happiness > self.happiness_warning:
            return "happy!"
        elif self.food <= self.food_warning:
            return "hungry:("
        else:
            return "bored:("

    def state(self):
        self.__state_change__()
        print("I'm a " + self.animal_type + ", my name is " + self.name + ", I feel " + self.mood)
        print("Food: " + str(self.food) + "/100")
        print("Happiness: " + str(self.happiness) + "/100")
        print("Vocabulary: ", self.vocabulary)

    def talk(self):
        """Prints a random word from the vocabulary"""
        print(self.vocabulary[randrange(len(self.vocabulary))])

    def feed(self):
        """Increases the food parameter by a random number"""
        self.food += randrange(self.food_maximum)
        print("om-nom-nom...\nThank you!")

        if self.food >= self.food_maximum:
            self.food = self.food_maximum
            print("I'm full!")
        elif self.food <= 0:
            self.food = 0
            print("I'm still hungry!")

        self.__state_change__()

    def play(self):
        """Increases the happiness parameter by a random number"""
        self.happiness += randrange(self.happiness_maximum)
        print("wohoo!")

        if self.happiness >= self.happiness_maximum:
            self.happiness = self.happiness_maximum
            print("I'm happy!")
        elif self.happiness <= 0:
            self.happiness = 0
            print("I'm bored:(")

        self.__state_change__()


def main():
    animal_type = input("Choose an animal type for your pet: ")
    name = input("Choose a name for your pet: ")

    tamagotchi = Tamagotchi(animal_type, name)
    input("Press enter to start")

    command = None

    while command != "0":
        print(
            """
            Choose an option to interact with your pet:
            0 - quit
            1 - feed your pet
            2 - play with your pet
            3 - check the state of your pet
            4 - teach your pet a new word
            5 - talk with your pet
            """
        )
        command = input("Command: ")

        if command == "0":
            print("Bye!")
        elif command == "1":
            tamagotchi.feed()
        elif command == "2":
            tamagotchi.play()
        elif command == "3":
            tamagotchi.state()
        elif command == "4":
            new_word = input("What word do you want to teach your pet? ")
            tamagotchi.learn_word(new_word)
        elif command == "5":
            tamagotchi.talk()
        else:
            print("There is not such command, sorry:( Try again")


main()
