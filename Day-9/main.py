import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

done = False
auction_dict = {}
print(logo)
print("Welcome to the secret auction program.")
while not done:
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    
    auction_dict[name] = bid

    if (input("Are there any other bidders? Type 'yes' or 'no'.\n") == "yes"):
        os.system('clear')
    else:
        done = True
        os.system('clear')
        
highest_bid = max(zip(auction_dict.values(), auction_dict.keys()))[1]
print(f"The highest bidder is {highest_bid} with a bid of : ${auction_dict[highest_bid]}")
            
