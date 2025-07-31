import random

subjects=[
    "Sharuk khan",
    "virat kholi",
    "Chandan",
    "Cat",
    "Rikshah vala"
]

actions=[
    "launches",
    "Declared war",
    "cancel",
    "eats",
    "dances with",
    "orders",
    "celebrates"
]
 

places=[
    "at Red Fort",
    "in local train",
    "a plate of samosa",
    "during ipl match",
    "at ganga ghat",
    "at India Gate"
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places)

    headline=f"Breaking News: {subject} {action} {place}"

    print("\n" + headline)

    user_input=input("\nDo you want to another headline? (yes / no)").strip().lower()
    if user_input=="no":
        break

print("\n Thankyou for using the fake news generator app")