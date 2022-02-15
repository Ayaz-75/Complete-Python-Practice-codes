











bids={
    "Ayaz":234,
    "Zahoor":324
}
bidding_finished=False

def highest_bidder(bidding_record):
    highest_bid=0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"winner is {winner} with bid ${highest_bid}")

while not bidding_finished:
    name=input("Enter your name\n")
    bid_price=int(input("Enter bid price\n"))
    bids[name]=bid_price
    should_continue=input("Are there any other bidding users ?")
    if should_continue=="no":
        bidding_finished =True
    elif should_continue=="yes":
        bidding_finished =False
highest_bidder(bids)