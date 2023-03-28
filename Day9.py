from replit import clear
from supportFiles.day9art import logo

print(logo)
reiterate = True
bidders = {}
winner_name = None
winner_bid = 0

while reiterate is not False:
    key = input('Please state your name: \n')
    bidders[key] = int(input('Please state the bid amount: \n'))
    reiterate_input = input('Is there any other bidders? Yes or No \n')
    if reiterate_input.lower() == "yes":
        reiterate = True
        clear()
    elif reiterate_input.lower() == "no":
        reiterate = False

for key in bidders:
    bidderValue = bidders[key]
    if bidderValue > winner_bid:
        winner_bid = bidderValue
        winner_name = key

print("The Winner is {} with a bid amount of {}".format(winner_name,winner_bid))


