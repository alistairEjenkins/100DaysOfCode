# Choose Your Own Adventure


print("You're washed up on a golden beach. Ahead of you is the entrance to a dark cave"
      ", to your left are mangroves and your right slippery rocks. Where to next?")
choice1 = input("Choose: cave, grove, rocks\n>>")
if choice1 == 'cave':
    print("You trudge up the beach and colapse exhausted on a rock at the entrance to the cave. After passing out for how long you wake to hear the 'CLINK, CLINK' of metal being struck inside the cave. Do you enter the dark cave to investigate or returnto the beach?")
    choice2 = input("Where to next? cave/beach?")
elif choice1 == 'grove':
    print('mangroves')
elif choice1 == 'rocks':
    print('rocks')

if choice2 == 'cave':
    print('inside cave')
else:
    print('beach')