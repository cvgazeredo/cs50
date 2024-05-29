# Prompt user for a positive interger between 0 to 8:
while True:
    height = input("Height: ")
    if not height.isnumeric():
        continue
    height = int(height)
    if height > 0 and height <= 8:
        break

# Print the pyramid:
for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)
