print("MIRRORED TRIANGLE")
num_row = int(input("Enter the number of rows: "))

for i in range(num_row):
    for j in range(i + 1):
        print("* ", end = "")
    print()

for i in range(num_row):
    for j in range(num_row - i):
        print("* ", end = "")
    print()
