bids ={}
continue_bidding= True

def find_higest_bidder(bidding_dictionary):
   highest_bid = 0
   winner=""

   max(bidding_dictionary)

   for bidder in bidding_dictionary:
      bid_amount = bidding_dictionary[bidder]
      if bid_amount > highest_bid:
         highest_bid = bid_amount
         winner = bidder

   print(f"{winner} is winner with bid of {highest_bid}$")
bids={}   

while continue_bidding:
   name = input("what is your good name :")
   price = int(input("what is your bidding amount : $"))
   bids[name] = price
   should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

   if should_continue == 'no':
      continue_bidding= False
      find_higest_bidder(bids)
   elif should_continue == 'yes':
      print("\n" * 250)
      
      
      
