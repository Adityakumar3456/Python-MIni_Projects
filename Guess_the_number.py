import random

'''Random number generator Game'''

ran=random.randint(1,100)

while True:
    num = int(input("Guess the number or Quit(Q): "))
    if(num == ran):
        print("The number is correct", ran)
        break
    
    elif(num< ran):
        print("The number is too small")
    else:
        print("the number is too big")

print("----Game Over----")

