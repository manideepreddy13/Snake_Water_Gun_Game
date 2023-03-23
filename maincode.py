import random


def decidefac(us, com):
    if(us == com):
        return None

    elif(us == 's'):
        if(com == 'w'):
            return True
        elif(com == 'g'):
            return False

    elif(us == 'w'):
        if(com == 's'):
            return False
        elif(com == 'g'):
            return True

    elif(us == 'g'):
        if(com == 'w'):
            return False
        elif(com == 's'):
            return True


n = random.randint(1, 3)
print("Please Wait!! It's Computer's Turn.")
us = input("It's your Turn\nEnter your choice\nValid Choices: s,w,g\n")

if(us != 's' and us != 'w' and us != 'g'):
    us = input("Invalid Choice!!! Please Enter Again\n")


if(n == 1):
    com = 's'

elif(n == 2):
    com = 'w'

elif(n == 3):
    com = 'g'


res = decidefac(us, com)


print(f"Computer chose {com}. Therefore,")


if(res == None):
    print("It's a Tie")
elif(res == True):
    print("You Won")
elif(res == False):
    print("You Lost")
