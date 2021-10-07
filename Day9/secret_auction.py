#ans=input("Are there any more bidders?")
bidders={}
i=0
while i<3:
    ans=input("Are there any more bidders?  ")
    name=input("enter your name  ")
    price=int(input("Enter the bidding price  "))
    bidders[name]=price
    i+=1
for name, price in bidders.items():
    if price==max(bidders.values()):
        print(f"The winner of the auction is {name} with price {price}")
        
