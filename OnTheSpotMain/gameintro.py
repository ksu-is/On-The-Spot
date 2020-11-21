print('Welcome to On The Spot! Please have fun/')
# begining the game. asking if wanting to start then importing questions
#TODO: 
#[ ] add structure to introduction
#[ ] blueprint for opening sequence and game flow
#[ ] begin adding variables and references, crossing game flow from imported questions.py and basegamescript.py

response = input("Press 'R' if ready to take the quiz or 'Q' to quiz\n")

if response.lower() == 'R':
    import pytrivia #currently non-functional
elif response.lower() == 'Q':
    print("Thank you for playing")
else:
    print("You did not choose a valid option")

# Need to refine the above sequencing for game start; follow up with player setup, before entering gameplay