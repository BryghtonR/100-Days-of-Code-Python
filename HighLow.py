#100 Days of Coding Day 14: High Low Guessing Game (modified for historical dates: 1900's)
import random
import os

#replay loop
play_again = "y"
while play_again == "y":
    os.system('cls')

    #base dictionary
    dict_of_events = {
        "The Start of World War 2": 1939,
        "Women gained the right to vote": 1920,
        "Dropping the atomic bomb on Hiroshima": 1945,
        "Passage of the Civil Rights Act": 1964,
        "The Start of World War 1": 1914,
        "Landing a man on the Moon": 1969,
        "Assassination of President Kennedy": 1963,
        "Fall of the Berlin Wall": 1989,
        "Start of the U.S. Great Depression": 1929,
        "Breakup of the Soviet Union": 1991,
        "Start of the Vietnam War": 1955,
        "Charles Lindergh's transatlantic flight": 1927,
        "Launching of the Russian Satellite Sputnik": 1957,
        "Start of the Korean War": 1950,
        "Start of the Persian Gulf War": 1991,
    }

    #Function: print out events and associated date
    def events_print():
        print(f"{event_main} : {dict_of_events[event_main]}")
        print(f"{event_compare} : {dict_of_events[event_compare]}")

    #setup initial events and streak
    event_compare = random.choice(list(dict_of_events))
    streak = True
    streak_count = 0
    #run quiz series
    while streak == True:

        #bump and select events
        event_main = event_compare
        event_compare = random.choice(list(dict_of_events))
        #duplicate checker
        while event_main == event_compare:
            event_compare = random.choice(list(dict_of_events))

        #Quiz question
        print(f"Your Current Streak Count is {streak_count}")
        compare = input(f"Did {event_main} happen BEFORE {event_compare}? y/n: ")

        #Results
        events_print()
        if dict_of_events[event_main]< dict_of_events[event_compare] and compare == "y":
            print("Correct")
            streak_count +=1
        elif dict_of_events[event_main]> dict_of_events[event_compare] and compare == "n":
            print("Correct")
            streak_count +=1
        else:
            print("Incorrect")
            streak = False
            print(f"Final Streak was {streak_count}")
    #replay?
    play_again = input("Would you like to play again? y/n: ")
