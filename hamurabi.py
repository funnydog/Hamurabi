#!/usr/bin/env python3

import random

print("{:^80}".format("HAMURABI"))
print("{:^80}\n\n".format("CREATIVE COMPUTING MORRISTOWN, NEW JERSEY"))
print("{:^80}".format("Try your hand at governing ancient Sumeria"))
print("{:^80}\n".format("for a ten-year term of office"))

# variables
harvest = 3000
seeds = 2800
rats  = harvest - seeds
dead = 0
incoming = 5
people = 95 + incoming - dead
seeds_per_acre = 3
acres = harvest // seeds_per_acre
plague = False

# stats
percent_starved = 0.0
total_dead = 0

def show_report() -> None:
    global year, dead, incoming
    global plague, people, acres, seeds_per_acre, rats, seeds
    print("\n\n\nHamurabi: I Beg To Report To You,")
    print(f"In Year { year }, { dead } people starved, { incoming } came to the city")

    if plague:
        print("A horrible plague struck! Half of the people died.")

    print(f"Population is now { people }.")
    print(f"The city now owns { acres } acres.")
    print(f"You harvested { seeds_per_acre } bushels per acre.")
    print(f"The rats ate { rats } bushels.")
    print(f"You now have { seeds } bushels in store.\n")

def read_int(prompt: str) -> int:
    try:
        value = int(input(prompt))
    except ValueError:
        value = 0

    if value < 0:
        print("Hamurabi: I cannot do what you wish.")
        print("Get yourself another steward!!!")
        exit(0)

    return value

for year in range(1, 10+1):
    show_report()

    acre_value = random.randrange(17, 27)
    print(f"Land is trading at { acre_value } bushels per acre.")

    # buy
    while True:
        buy = read_int("How many acres do you wish to buy? ")
        if acre_value * buy > seeds:
            print("Hamurabi: Try again, you have only")
            print(f"{ seeds } bushels of grain. Now then,")
        else:
            break
    acres += buy
    seeds -= acre_value * buy

    # sell
    while True:
        sell = read_int("How many acres do you wish to sell? ")
        if sell > acres:
            print("Hamurabi: Try again, you have only")
            print(f"{ seeds } bushels of grain. Now then,")
        else:
            break
    acres -= sell
    seeds += acre_value * sell

    # feed
    while True:
        feed = read_int("How many bushels do you wish to feed your people? ")
        if feed > seeds:
            print("Hamurabi: Try again, you have only")
            print(f"{ seeds } bushels of grain. Now then,")
        else:
            break
    seeds -= feed

    # plant
    while True:
        plant = read_int("How many acres do you wish to plant with seeds? ")
        if plant > acres:
            print(f"Hamurabi: Think again. You only own { acres } acres. Now then,")
        elif plant // 2 > seeds:
            print(f"Hamurabi: Think again. You have only { seeds } bushels of grain. Now then,")
        elif plant > 10 * people:
            print(f"Hamurabi: But you have only { people } people to tend the fields! Now then,")
        else:
            break
    seeds -= plant // 2

    # a bountiful harvest
    seeds_per_acre = random.randrange(1, 7)
    harvest = plant * seeds_per_acre

    # rats
    rats_odds = random.randrange(1, 7)
    if rats_odds & 1 == 1:
        rats = seeds // rats_odds
    else:
        rats = 0

    seeds = seeds + harvest - rats

    # new people
    incoming = random.randrange(1, 7) * (20 * acres + seeds) // (people * 100) + 1

    # full tummies
    people_fed = feed // 20
    dead = (people > people_fed) and (people - people_fed) or 0

    # starve enough for impeachment?
    if dead * 100 > people * 45:
        print(f"You starved { dead } people in one year!!!")
        print("Due to this extreme mismanagement you have not only")
        print("been impeached and thrown out of office but you have")
        print("also been declared national fink!!!")
        exit(0)

    percent_starved = ((year-1) * percent_starved + dead * 100 / people) / year
    total_dead += dead
    people -= dead
    people += incoming

    # 15% chance of plague
    plague = random.randrange(20) < 3
    if plague:
        people //= 2

# end
show_report()

avg_acres = acres / people
print(f"In your 10-year term of office {percent_starved:.2f} percent of the")
print("population starved per year on the average, i.e. a")
print(f"total of { total_dead } people died!!!")
print("You started with 10 acres per person and ended with")
print(f"{avg_acres:.2f} acres per person.\n")

if percent_starved > 33 or avg_acres < 7:
    print("Due to this extreme mismanagement you have not only")
    print("been impeached and thrown out of office but you have")
    print("also been declared national fink!!!")
elif percent_starved > 10 or avg_acres < 9:
    print("Your heavy-handed performance smacks of Nero and Ivan IV.")
    print("The people (remaining) find you an unpleasant ruler, and,")
    print("frankly, hate your guts!!!")
elif percent_starved > 3 or avg_acres < 10:
    print("Your performance could have been somewhat better, but")
    print("really wasn't too bad at all.", int(random.uniform(0, 0.8) * people), " people")
    print("would dearly like to see you assassinated but we all have our")
    print("trivial problems.")
else:
    print("A fantastic performance!!! Charlemagne, Disraeli and")
    print("Jefferson combined could not have done better!")

