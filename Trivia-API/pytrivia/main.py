from pytrivia import Category, Diffculty, Type, Trivia
my_api = Trivia(True)
response = my_api.request(2, Category.Books, Diffculty.Hard, Type.True_False)
print(response)