action = input("Do you like action movies? (yes/no): ").strip().lower() == "yes"
comedy = input("Do you like comedy movies? (yes/no): ").strip().lower == "yes"
drama = input("Do you like drama movies? (yes/no): ").strip().lower() == "yes"

if action and comedy and not drama:
    genre="Action-Comedy"
elif action and drama and not comedy:
    genre="Action-Drama"
elif comedy and drama and not action:
    genre="Comedy-Drama"
elif action and comedy and drama:
    genre="Action-Comedy-Drama"
elif action and not comedy and not drama:
    genre="Action"
elif comedy and not action and not drama:
    genre="Comedy"
elif drama and not action and not comedy:
    genre="Drama"
else:
    genre="No specific genre"

if genre == "No specific genre":
    print("You have a unique taste in movies! try asking a friend!")
elif genre == "Action":
    print("You may like these action movies: Mad Max: Fury Road, John Wick, Die Hard")
elif genre == "Comedy":
    print("You may like these comedy movies: Superbad, The Hangover, Step Brothers")
elif genre == "Drama":
    print("You may like these drama movies: The Shawshank Redemption, Forrest Gump, The Godfather")
elif genre == "Action-Comedy":
    print("You may like these action-comedy movies: Guardians of the Galaxy, deadpool")
elif genre == "Action-Drama":
    print("You may like these action-drama movies: Gladiator, The Dark Knight")
elif genre == "Comedy-Drama":
    print("You may like these comedy-drama movies: The Grand Budapest Hotel, Little Miss Sunshine")
os.execl(sys.executable, sys.executable, *sys.argv)