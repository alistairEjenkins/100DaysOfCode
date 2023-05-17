# Choose Your Own Adventure


choice1 = input("red, blue, yellow doors")
if choice1 == 'red':
    print("you die! lava floor")
elif choice1 == 'blue':
    print("pool of water")
    choice2 = input("swim to other side, dive to bottom")
    if choice2 == 'swim':
        choice3 = input("wooden door - open/knock?")
        if choice3 == 'open':
            print('you die! spikes')
        else:
            print("pool drains, avoid man-eating octopus + collect treasure")
    else:
        print("You die! eaten by octopus ")
else:
    print("escape to beach")