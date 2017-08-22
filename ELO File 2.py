__author__ = 'Joe'
from random import randint
#Runs an ELO Rated System

# Variables
k = 32
starting_score = 1400
players = {}

# Player set up function
def create_players(initial_score):
    print("To start an ELO rated system, you will need to add at least two players.\n")
    name = str(input("Enter name of first player: "))
    players[str(name)] = initial_score
    name = str(input("Enter name of second player: "))
    players[str(name)] = initial_score
    choice = str(input('Add another player? (y/n) ')).lower()
    while choice != 'y' and choice != 'n':
        choice = str(input("That's not a valid answer, type 'y' or 'n'. Enter again: ")).lower()
    while choice == 'y':
        name = str(input("Enter name of new player: "))
        initial_score = 1400
        players[str(name)] = initial_score
        choice = str(input('Add another player? (y/n) ')).lower()
        while choice != 'y' and choice != 'n':
            choice = str(input("That's not a valid answer, type 'y' or 'n'. Enter again: ")).lower()
    print("")
    print("Ok, here is your list of players and their respective ratings: ")
    for x in players:
        print(x+", rating: "+str(players[x]))
    print("")


# Add a player function
def add_a_player():
    choice = 'y'
    while choice == 'y':
        name = str(input("Enter name of new player: "))
        initial_score = 1400
        players[str(name)] = initial_score
        choice = str(input('Add another player? (y/n) ')).lower()
        while choice != 'y' and choice != 'n':
            choice = str(input("That's not a valid answer, type 'y' or 'n'. Enter again: ")).lower()
    print("")
    print("Ok, here is your list of players: ")
    for x in players:
        print(x+", rating: "+str(players[x]))
    print("")

# Update ratings with random matchups function
def update_random():
    again = 'y'
    while again == 'y':
        if (len(players)) < 2:
            print("You haven't got enough players! Go back and add at least two players.")
            again = 'n'
        else:
            players_list = list(players.keys())
            i = randint(0, int(len(players_list))-1)
            playerA = players_list[i]
            players_list.pop(i)
            j = randint(0, int(len(players_list))-1)
            playerB = players_list[j]
            R_A = players[playerA]
            R_B = players[playerB]
            E_A = (1/(1+10**((R_A-R_B)/400)))
            E_B = (1/(1+10**((R_B-R_A)/400)))
            print(str(playerA)+" vs. "+str(playerB))
            winner = str(input("Enter winner (or enter 'draw' if it is a draw): ")).lower()
            while winner != playerA.lower() and winner != playerB.lower() and winner != "draw":
                winner = str(input("You need to enter the exact fullname of the winner of the matchup, or 'draw'."
                                   " Enter again: ")).lower()
            if winner == playerA.lower():
                players[playerA] = R_A+k*(1-E_A)
                players[playerB] = R_B-k*E_B
            elif winner == playerB.lower():
                players[playerA] = R_A-k*E_A
                players[playerB] = R_B+k*(1-E_B)
            else:
                players[playerA] = R_A+k*(0.5-E_A)
                players[playerB] = R_B+k*(0.5-E_B)
            again = str(input('Play another game? (y/n) ')).lower()
            print("")
        while again != 'y' and again != 'n':
            again = str(input("That's not a valid answer, type 'y' or 'n'. Enter again: ")).lower()

# Update ratings with selective matchups function
def update_selective():
    again = 'y'
    while again == 'y':
        if (len(players)) < 2:
            print("You haven't got enough players! Go back and add at least two players.")
        else:
            playerA = str(input("Enter the name of the first player: "))
            players_list = list(players.keys())
            while not(playerA in players_list):
                playerA = str(input("The player you entered isn't in the tournament. Be sure to capitalise letters"
                                    " correctly. Enter again: "))
            playerB = str(input("Enter the name of the second player: "))
            while not(playerB in players_list) or playerA == playerB:
                playerB = str(input("The player you entered isn't in the tournament, or you tried to make a player"
                                    " verse themselves. Be sure to capitalise letters correctly. Enter again: "))
            R_A = players[playerA]
            R_B = players[playerB]
            E_A = (1/(1+10**((R_A-R_B)/400)))
            E_B = (1/(1+10**((R_B-R_A)/400)))
            print(str(playerA)+" vs. "+str(playerB))
            winner = str(input("Enter winner (or enter 'draw' if it is a draw): ")).lower()
            while winner != playerA.lower() and winner != playerB.lower() and winner != "draw":
                winner = str(input("You need to enter the exact fullname of the winner of the matchup, or 'draw'."
                                   " Enter again: ")).lower()
            if winner == playerA.lower():
                players[playerA] = R_A+k*(1-E_A)
                players[playerB] = R_B-k*E_B
            elif winner == playerB.lower():
                players[playerA] = R_A-k*E_A
                players[playerB] = R_B+k*(1-E_B)
            else:
                players[playerA] = R_A+k*(0.5-E_A)
                players[playerB] = R_B+k*(0.5-E_B)
            again = str(input('Play another game? (y/n)')).lower()
        while again != 'y' and again != 'n':
            again = str(input("That's not a valid answer, type 'y' or 'n'. Enter again: ")).lower()

# View Players and Ratings function
def view_players():
    view_method = str(input("Do you want to view in alphabetical order, or by descending order of rating? Enter"
                                " 'alphabetically' or 'rating': ")).lower()
    while True:
        if view_method == 'alphabetically':
            players_list = list(players.keys())
            players_list.sort()
            print("")
            print("Here is your list of players and their respective ratings: ")
            for x in players_list:
                print(x+", rating: "+"%.2f" % players[x])
            print("")
            break
        elif view_method == 'rating':
            print("")
            players_sorted_list = sorted(players, key=players.get, reverse=True)
            print("Here is your list of players and their respective ratings: ")
            for x in players_sorted_list:
                print(x+", rating: "+"%.2f" % players[x])
            print("")
            break
        else:
            view_method = str(input("You didn't select one of the options. Enter 'alphabetically' or"
                                    " 'rating': ")).lower()

# Reset Ratings function
def reset_ratings(initial_score):
    for x in players:
        players[x] = initial_score
    print("All ratings have been reset to " + str(starting_score))
    print("")

# End Tournament function
def end():
    print("You have finished your tournament. These were your final rankings:")
    for x in players:
        print(x+", rating: "+"%.2f" % players[x])

# Main
create_players(starting_score)
while True:
    answer = str(input("Add a player\n"
                       "Update ratings with random matchups\n"
                       "Update ratings with selective matchups\n"
                       "View players and ratings\n"
                       "Reset ratings\n"
                       "End tournament\n"
                       "\n"
                       "Enter one of the above options: ")).lower()
    print("")

    if answer == "add a player":
        add_a_player()
    elif answer == "update ratings with random matchups":
        update_random()
    elif answer == "update ratings with selective matchups":
        update_selective()
    elif answer == "view players and ratings":
        view_players()
    elif answer == "reset ratings":
        reset_ratings(starting_score)
    elif answer == "end tournament":
        end()
        break
    else:
        print("")
        print("You didn't select one of the options. Try again and make sure you type it out exactly.")
