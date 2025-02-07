def madlib():   #define a function named Madlib
    print("Welcome to the Madlibs game!")    #Greatings massage when we call function
    
    # Asking the user for different types of words
    adjective1 = input("Enter an adjective ('Hint funny'): ") #Enter an adjective: funny
    noun1 = input("Enter a noun ('Hint cat or dog'): ")  #enter a noun: cat
    verb1 = input("Enter a verb (past tense)('Hint jumped'): ")  #Enter a verb (past tense): jumped
    adjective2 = input("Enter another adjective('Hint big'): ") #Enter another adjective: big
    noun2 = input("Enter another noun('Hint ball'): ") #eter another noun: ball
    place = input("Enter a place ('Hint park'): ") #Enter a place: park
    verb2 = input("Enter another verb (present tense) ('Hint play'): ")  #Enter another verb (present tense): play
    
    # Creating a story verible using the inputs
    story = f"Once upon a time, in a {adjective1} land, there was a {noun1} who loved to {verb1}. " \
            f"One day, the {noun1} discovered a {adjective2} {noun2} lying in the middle of {place}. " \
            f"Excited, the {noun1} decided to {verb2} and lived happily ever after!"
    
    # Printing the madlib story
    print("\nHere's your madlib story:\n")
    print(story)

# Call the function to start the game
madlib()
