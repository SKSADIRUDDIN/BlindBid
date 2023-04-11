from replit import clear
import art
con="yes"
bid={}
while(con=="yes" and con!="no"):
  print(art.logo)
  name=input("Enter Your Name: ")
  val=int(input("Enter your bid : Rs "))
  bid[name]=val
  con=input("Is there any other to bid type yes or no ")
  clear()
max=0
win=""
for key in bid:
  if(bid[key]>max):
    max=bid[key]
    win=key
print(f"The winner is {win} with a bid of Rs {max}")

#HINT: You can call clear() to clear the output in the console.