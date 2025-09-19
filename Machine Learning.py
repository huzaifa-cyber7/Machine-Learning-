target=220
guess=None
while guess !=target:
    guess=int(input("enter number"))
    if guess==target:
        print("target achieved")
    else:
        print("target not achieved")

