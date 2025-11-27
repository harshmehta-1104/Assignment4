string1 = str(input("Enter text to write to the file: "))

with open("task2.txt", "wt") as fh:
    fh.write(string1)
    fh.write("\n")
    print("Data successfully written to output.txt. \n")

string2 = str(input("Enter additional text to append:"))
with open("task2.txt", 'at') as fh:
    fh.write(string2)
    print("Data successfully appended. \n")

print("Final content of output.txt: ")
try:
    with open("task2.txt", 'rt') as fh:
        print(fh.readline().rstrip("\n"))
        print(fh.readline())

except FileNotFoundError:
    print("File not found.")
