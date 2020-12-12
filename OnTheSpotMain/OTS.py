
import html
import json
import urllib.request


def generate_answers(quest, QuestionType):
    answers = []
    if QuestionType == "multiple":
        answers = [
            quest["correct_answer"],
            quest["incorrect_answers"][0],
            quest["incorrect_answers"][1],
            quest["incorrect_answers"][2]
        ]
        answers.sort()
    elif QuestionType == "boolean":
        answers = ["True", "False"]
    else:
        print("Unrecognized question type: " + QuestionType)
    return answers


def generate_questions(n, TOKEN, TOPIC, DIFFICULTY):
    QuestionURL = "https://opentdb.com/api.php?amount=" + \
        str(n) + "&token=" + TOKEN + TOPIC + DIFFICULTY

    with urllib.request.urlopen(QuestionURL) as url:
        data = json.loads(url.read().decode())
    return data


n = 10
TokenURL = "https://opentdb.com/api_token.php?command=request"

with urllib.request.urlopen(TokenURL) as url:
    data = json.loads(url.read().decode())
    TOKEN = data["token"]

TopicURL = "https://opentdb.com/api_category.php"

with urllib.request.urlopen(TopicURL) as url:
    data = json.loads(url.read().decode())
    cat = data["trivia_categories"]



def playerSetup():

    """  
    Welcome the player, and ask for names to initialize player profiles
    """
    print("\n       ------ !! Let's Get Started !! ------\n")
    
    while True:
        player_count = input("How many players will be participating? (2-4): ")
        if player_count.isalpha():
            print("Invalid Input.\n")
        else:
            player_count = int(player_count)
            if player_count < 2:
                print("Minimum 2 players required.\n")
            elif player_count > 4:
                print("Maximum 4 players allowed.\n")
            else:
                break

    for i in range(0, player_count):
        name = input("Player " + str(i+1) + ", Enter your name: ")
        name = name.title()
        players["player"+str(1+i)] = {'name': name, 'points': 0, 'streak': 0}
    return player_count, players

def gameRules():
    print("\n       ------ !! Welcome to On The Spot !! ------\n")
    print('The rules are simple. There are 9 rounds of trivia.\n')
    print('Each round will have 3 randomized catogories to choose from. Players will each choose their difficulty and answer the question.\n')
    print('For every 2 questions in a row correct, players will be given the opportunity for an "On The Spot" question.\n')
    print('The player with the most points wins.')
    
    player_status = ""
    while True:
        player_status = input("\nAre you ready to begin? (y/n): ")
        if player_status.lower() == 'y':
            print("Let's begin!")
            return
        elif player_status.lower() == 'n':
            print('Exiting game. Thank you.')
            exit()
        else:
            print("Invalid Input.")


def game_control():
    '''
    Control the whole game with the single steps.
    '''
    gameReset()
    playerSetup()
    gameRules()

game_control()
