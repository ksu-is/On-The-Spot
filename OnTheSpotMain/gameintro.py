print('Welcome to On The Spot! Please have fun/')
# begining the game. asking if wanting to start then importing questions

response = input("Press 'R' if ready to take the quiz or 'Q' to quiz\n")

if response.lower() == 'R':
    import pytrivia 
elif response.lower() == 'Q':
    return "Thank you for playing"
else:
    print("You did not choose a valid option")
    