import random
def game_score(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return True
        elif you == 'c':
            return False
    elif comp == 'p':
        if you == 'c':
            return True
        elif you == 's':
            return False
    elif comp == 'c':
        if you == 's':
            return True
        elif you == 'p':
            return False 

print("computer's turn stone(s), paper(p), sissor(c):")
rand_no = random.randint(1,3)
if(rand_no==1):
    comp ="s"
elif(rand_no == 2):
    comp ="p"
elif(rand_no==3):
    comp ="c"

you = input("your's turn stone(s), paper(p), sissor(c):")
a = game_score(comp, you)

print(f"computer choose  {comp}")
print(f"computer choose  {you}")

if a== None:
    print("The game is tie")
elif a:
    print("you win")
else:
    print("you lost")

