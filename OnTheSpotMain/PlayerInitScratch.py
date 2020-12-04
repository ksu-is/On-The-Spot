# players = {
#     "player1" : {
#         "name" : "",
#         "points" : [],
#         "streak" : 0
#     },
#     "player2" : {
#         "name" : "",
#         "points" : [],
#         "streak" : 0
#     }
# }
players = {}

player_count = input("How many players?: ")
player_count = int(player_count)

for pl in range(player_count):
    name = input("Enter your name: ")
    players[pl]["name"] = name
    players[pl]["points"] = 0
    players[pl]["streak"] = 0

print(players)
# print(players["player2"]["name"])
# players["player2"].update({"name": "Alicia"})
# print(players["player2"]["name"])
#Just testing dictionary commands. Trying to figure out how to iterate through the range of player count to set up a dictionary for each new player

#Testing different ways to format the dictionary for each player. It probably needs to start with an empty dictionary, I think.
#I commented out the nested dictionary, but left it bc that's how I'm looking to format it currently. But still testing