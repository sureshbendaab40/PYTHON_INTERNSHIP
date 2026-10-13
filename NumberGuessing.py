# start = int(input("enter a nunber : "))
# end = int(input("enter sencond nu ber : "))
# while start <= end :
#     i =2
#     while i<start:
#         if start % i != 0:
#             print(start)
#             start +=1
#         else:
#             continue    
            
import random 
#print(random.randint(1,50))
v = random.randint(1,50)
chance = 0
while chance < 5:
    guess = int(input("GUESS A NO RANDOM BETWEEN (1,50) :"))
    if guess> 50:
        print("PLZZ SELECT NO BETWEEN 1-50 ONLY THANK YOU AND TRY AGAIN . ")
        if chance > 5:
            chance -=1
    else :
        if v==guess :
            print("😍😍😍😍😍 YAY YOU ARE WINNER : GOOD LUCK BRO 😍😍😍😍😍. ")
            break 
        elif v < guess:
            print("🤔🤔🤔🤔 THINK SMALL NO. AND TRY AGAIN GOOD LUCK. 🤔🤔🤔🤔")
        elif v > guess:
            print("🤔🤔🤔🤔 THINK BIG NO. AND TRY AGAIN GOOD LUCK.🤔🤔🤔🤔")
        # else: 
        #     print(" TRY AGAIN ")
        chance +=1    
    
        
        