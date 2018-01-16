import random

print("If you want get advice type the space and enter")

ans1="wait"
ans2="don't do that"
ans3="gogo!"
ans4="you can do it"
ans5="Did you say you were thinking that?"
ans6="cheer up!"
ans7="sometimes you get obstacle but you can overcome"
ans8="....nono"

if input(""):
    print("Thinking...\n"*4)

    choice=random.randint(1,8)
    if choice==1:
        answer=ans1
    elif choice==2:
        answer=ans2
    elif choice==3:
        answer=ans3
    elif choice==4:
        answer=ans4
    elif choice==5:
        answer=ans5
    elif choice==6:
        answer=ans6
    elif choice==7:
        answer=ans7
    else:

        answer=ans8

    print(answer)

    input("\n\n if you want go out enter the enter")
        

