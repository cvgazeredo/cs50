from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)
# Lists have a function built into them, (and functions built into objects
# know as methods) where a function kinf of stands on its own

average = sum(scores) / len(scores)
print(f"Average: {average}")