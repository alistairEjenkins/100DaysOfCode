# coin toss

import random

face_choice = random.randint(0,1)
if face_choice == 0:
    print('heads')
else:
    print('tails')

print(random.choice(['heads', 'tails']))