"""clickbait generator by Hamissi"""

import random

# set up the constants
OBJECT_PRONOUNS = ["Her", "Him", "Them"]
POSSESIVE_PRONOUNS = ["Her", "His", "Their"]
PERSONAL_PRONOUNS = ["She", "He", "They"]
STATES = ["Kwa-Zulu Natal", "Mpumalanga", "North-West", "Limpopo", "Gauteng", "Eastern Cape", "Western Cape",
          "Northern cape", "Free-State"]
NOUNS = ["Athlete", "Clown", "Shovel", "Paleo Diet", "Doctor", "Parent", "Cat", "Dog",
         "Chicken", "Robot", "Video Game", "Avocado", "Plastic Straw",
         "Serial Killer", "Telephone psychic"]
PLACES = ["House", "Attic", "Bank Deposit Box", "School", "Basement",
          "Workplace", "Donut Shop", "Apocalypse Bunker"]
WHEN = ["Soon", "This Year", "Later Today", "RIGHT NOW", "Next Week"]


def main():
    print("ClickBait Headline Generator")
    print("By Hamissi")
    print()

    print("Our website needs to trick people into looking at ads!")
    while True:
        print("Enter the number of clickbait headlines to generate")
        response = input("> ")
        if not response.isdecimal():
            print("Please enter a number. ")
        else:
            numberOfHeadlines = int(response)
            break  # Exit the loop once a valid number is entered.

    for i in range(numberOfHeadlines):
        clickBaitType = random.randint(1, 8)

        if clickBaitType == 1:
            headline = generateAreMillenialsKillingHeadline()
        elif clickBaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickBaitType == 3:
            headline == generateBigCompaniesHateHerHeadline()
        elif clickBaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickBaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickBaitType == 6:
            headline = generateGiftHeadline()
        elif clickBaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickBaitType == 8:
            headline = generateWhatYouDontKnowHeadline()
        elif clickBaitType == 9:
            headline = generateJobAutomatedHeadline()

        print(headline)

        website = random.choice(["wobsite", "blag", "Facebuuk", "Googles", "Facesbook", "Tweedie", "Pastagram"])

        when = random.choice(WHEN).lower()
        print("Post these to ,{} , {}, 'or you're fired!!'".format(website, when))


# Each of these functions returns a different type of headline
def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return "Are Millenials Killing the {} Industry?".format(noun)


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + "s"
    when = random.choice(WHEN)
    return "Without This {}, {} Could Kill You {}".format(noun, pluralNoun, when)


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return "Big Companies Hate {}!! See How This {} {} Invented a Cheaper {}".format(pronoun, state, noun1, noun2)


def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return "What {} don't want you to know about {}".format(state, noun, pronoun, place)


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + "s"
    pluralNoun2 = random.choice(NOUNS) + "s"
    return "What {} Don't Want you to know about {}".format(pluralNoun1, pluralNoun2)


def generateGiftHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return "{} Gift Ideas to give your {} from {}".format(number, noun, state)


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + "s"
    # Number 2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return "{} Reasons Why {} Are more interesting than you think (number {} will surprise you)".format(number1,
                                                                                                       pluralNoun,
                                                                                                       number2)


def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == "Their":
        return "This {} {} Didn't Thing robots would take {} Job. {} were wrong. ".format(state, noun, pronoun1,
                                                                                          pronoun2)
    else:
        return "This {} {} Didn't Think Robots Would Take {} Job. {} Was Wrong".format(state, noun, pronoun1, pronoun2)


# if the program is run (instead of imported), run the game
if __name__ == "__main__":
    main()
