# 1- import the random  module
import random

# 2- create subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "Celebrates"
]



places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "Taj Mahal",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

politics = [
    "inside Parliament House",
    "at a political rally in Uttar Pradesh",
    "during a heated Lok Sabha debate",
    "outside Election Commission office",
    "in a cabinet meeting",
    "at Jantar Mantar protest site",
    "during the budget announcement"
]


# 3- Starts the headline generation loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    politic = random.choice(politics)
 

    headline = f"BREAKING NEWS: {subject} {politic} {action} {place_or_thing}  "
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break
     
# print goodbye message
print("\nThanks for using the Fake Headline Generator. Have a nice day")
