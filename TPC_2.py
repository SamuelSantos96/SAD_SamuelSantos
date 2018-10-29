# Array of the cards that made a full deck
cards = ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "DC", "VC", "RC", "1P", "2P", "3P", "4P", "5P",
         "6P", "7P", "8P", "9P", "10P", "DP", "VP", "RP", "1O", "2O", "3O", "4O", "5O", "6O", "7O", "8O", "9O", "10O",
         "DO", "VO", "RO", "1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E", "9E", "10E", "DE", "VE", "RE"]


# Function that will count the amount of decks that exist from an array
def count_decks(my_cards):
    # Array for counting the amount of times a specific card appears based on the index of the array 'cards'
    counted_cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # For loop to iterate every card that exists from the array of the user
    for my_card in my_cards:
        # For loop to iterate every card that exists in the array 'cards'
        for i in range(len(cards)):
            # Verifies if the card the user has, matches the card from the array 'cards'
            if my_card == cards[i]:
                # Increments the amount of times the card was counted
                counted_cards[i] += 1

    # Declaration and Initialization of the the number of decks based
    # on the number of times the very first card was counted
    counted_number = counted_cards[0]

    # For loop to iterate the array 'counted_cards'
    for card_counted in counted_cards:
        # Verifies if the amount of times a specific card was counted less that the 'counted_number'
        if counted_number > card_counted:
            # Assigns the new value to 'counted_number'
            counted_number = card_counted

    # Displays the number of full decks that exist based on the array of the user
    if counted_number == 1:
        # If there is only one full deck, it displays this message
        print("There is", counted_number, "completed deck")
    else:
        # If there are 0 full decks or more than one full deck, it displays this message
        print("There are", counted_number, "completed decks")


# First array to be tested
A = ["10P", "9E", "1C"]

# Calls the function 'count_decks' for the array 'A'
count_decks(A)

# Second array to be tested
B = ["1P", "1C", "1O", "2P", "2C", "2O", "2E", "3P", "3C", "3O",
     "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O",
     "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP",
     "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE",
     "1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E",
     "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C",
     "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE",
     "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C",
     "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E",
     "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C",
     "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE",
     "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE"]

# Calls the function 'count_decks' for the array 'B'
count_decks(B)

# Third array to be tested
C = ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "DC", "VC", "RC", "1P", "2P", "3P", "4P", "5P", "6P",
     "7P", "8P", "9P", "10P", "DP", "VP", "RP", "1O", "2O", "3O", "4O", "5O", "6O", "7O", "8O", "9O", "10O", "DO", "VO",
     "RO", "1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E", "9E", "10E", "DE", "VE", "RE"]

# Calls the function 'count_decks' for the array 'C'
count_decks(C)

# Fourth array to be tested
D = ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "DC", "VC", "RC", "1P", "2P", "3P", "4P", "5P", "6P",
     "7P", "8P", "9P", "10P", "DP", "VP", "RP", "1O", "2O", "3O", "4O", "5O", "6O", "7O", "8O", "9O", "10O", "DO", "VO",
     "RO", "1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E", "9E", "10E", "DE", "VE", "RE", "1C", "2C", "3C", "4C", "5C",
     "6C", "7C", "8C", "9C", "10C", "DC", "VC", "RC", "1P", "2P", "3P", "4P", "5P", "6P",
     "7P", "8P", "9P", "10P", "DP", "VP", "RP", "1O", "2O", "3O", "4O", "5O", "6O", "7O", "8O", "9O", "10O", "DO", "VO",
     "RO", "1E", "2E", "3E", "4E", "5E", "6E", "7E", "8E", "9E", "10E", "DE", "VE", "RE"]

# Calls the function 'count_decks' for the array 'D'
count_decks(D)
