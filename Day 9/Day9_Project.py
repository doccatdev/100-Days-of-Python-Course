from art import logo

print(logo)

def bid_auction():
    d_bidauction = {}  # Dictionary to store bids
    max_value = 0  # Max bid value
    max_key = None  # Max bid key
    
    while True:  # Loop to allow multiple bids
        print('\n')
        user_name = input("What is your name: ")  # Get username as key
        bid_nominal = int(input("What is your bid: $"))  # Get bid as value

        # Add the key-value pair to the dictionary
        d_bidauction[user_name] = bid_nominal

        # Ask if there are more bidders
        more_bidders = input("Are there any other bidders? Type (yes/no): ").strip().lower()
        if more_bidders != "yes":
            break  # Exit loop if no more bidders

    # Find the highest bidder
    for key, value in d_bidauction.items():
        if value > max_value:
            max_value = value
            max_key = key

    print(f"The winner is {max_key} with a bid of {max_value}")
    #return d_bidauction  # Return the dictionary

# Call the function 
bid_auction()

#call function print the bids dictionary result
# output = bid_auction()
# print(output)
