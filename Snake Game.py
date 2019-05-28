import random
lst = ["s","w","g"]
userrscore = 0
comsocre = 0
i = 0

while i < 10:
    rand = random.choice(lst)
    choice = input("Snake [s]\nWater [w]\nGun   [g] \n\nEnter Your Choice : ")
    if choice == "s" and rand == "w" or choice == "w" and rand == "g" or choice == "g" and rand == "s":
        print("User Won")
        print(f"Computer Choose : {rand}")
        userrscore += 1
        print(f"\t\t\t\tUser Total Wins {userrscore}")
        print(f"\t\t\t\tComputer Total Wins {comsocre}")

    elif choice == "s" and rand == "g" or choice == "w" and rand == "s" or choice == "g" and rand == "w":
        print("Computer Won")
        print(f"Computer Choose : {rand}")
        comsocre += 1
        print(f"\t\t\t\tUser Total Wins {userrscore}")
        print(f"\t\t\t\tComputer Total Wins {comsocre}")

    elif choice == rand:
        userrscore += 1
        comsocre += 1
        print("Both are Same !")
        print(f"Computer Choose : {rand}")
        print(f"\t\t\t\tUser Total Wins {userrscore}")
        print(f"\t\t\t\tComputer Total Wins {comsocre}")
        
    else:
        print("Invalid Character !!!")
    i = i + 1
    print()


print(f"Total User Wins {userrscore}")
print(f"Total Comture Wins {comsocre}")
if userrscore < comsocre:
    print("Computer Won The Series !!!")
elif userrscore > comsocre:
    print("User Won The Series !!!")
else:
    print("Match Ties !!!")

