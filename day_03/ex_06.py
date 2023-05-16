# love calculator.

def letter_counter(word, names):
    count = 0
    for letter in word:
        count += names.count(letter)

    return count

print("Welcome to the Love Calculator")
name1 = input("What is the name of the first person?\n>> ").lower()
name2 = input("What is the name of the second person?\n>> ").lower()

combined_names = name1 + name2

score = int(letter_counter('true', combined_names)) * 10\
        + letter_counter('love', combined_names)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos!")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")

