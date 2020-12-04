""" print('Welcome to On The Spot! Please have fun/')
# begining the game. asking if wanting to start then importing questions. We want to have a proper game start. 
# need to refine and perfect intro 
#TODO: 
#[ ] add structure to introduction
#[ ] blueprint for opening sequence and game flow
#[ ] begin adding variables and references, crossing game flow from imported questions.py and basegamescript.py

"""
 #************************************************# DELETE ABOVE


def game_reset():
    '''
    Reset all variables of the whole game for a new play
    '''
    

def game_setup():
    '''
    Welcome the player and ask for his or her name as long as he thinks is correct.
    '''

    print("\n       ------ !! Welcome to On The Spot !! ------\n")
    
    loopSetup = True
    while loopSetup:
        players = input("How many players? ")
        if players == "":
            players = "1"
        if (players.isalpha() == True or int(players) < 0):
            print("Not valid answer")
        else:
            players = int(players)
            print("0. All")
            for i in range(1, len(cat) + 1):
                print(str(i) + ". " + cat[i-1]["name"])






def game_control():
    '''
    Control the whole game with the single steps.
    '''
    game_reset()
    game_setup()

