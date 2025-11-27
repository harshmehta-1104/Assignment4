with open("task1.txt", "wt") as fh:
    fh.write("This is a sample text file. \n")
    fh.write("It contains multiple lines.")

try:
    with open("Assignment4/task1.txt", 'rt') as fh:
        print("Line 1:", fh.readline().rstrip("\n"))
        print("Line 2:", fh.readline())
except FileNotFoundError as error:
    print("Error: The file 'task2.txt' was not found.")
