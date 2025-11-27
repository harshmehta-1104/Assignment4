# Python Practice Tasks – Assignment 4

This assignment focuses on file handling in Python. The tasks help you practice creating, writing, appending, and reading from text files, as well as handling file-related errors using exceptions.

---

## Task 1 – Writing to a File and Reading Its Contents

### Description  
This program first creates a text file and writes multiple lines of text into it. Then, it attempts to open a file for reading and displays its contents line by line. The program also demonstrates how to handle situations where the file being read does not exist, using a `try-except` block.

### Concepts Practiced

- Opening a file in write mode to create and write text  
- Using the `with` statement to automatically manage file closing  
- Writing multiple lines to a text file  
- Opening a file in read mode and reading lines one at a time  
- Using `rstrip()` to clean newline characters from the end of a line  
- Handling `FileNotFoundError` with a `try-except` block  
- Printing meaningful error messages when a file cannot be found  

### Expected Behavior

- The program creates a text file and writes sample lines into it.  
- It then attempts to open a specified file and read the first two lines.  
- If the file is found, the lines are printed with clear labels.  
- If the file is not found, an error message is displayed instead of the program crashing.

---

## Task 2 – Writing, Appending, and Displaying File Content

### Description  
This program asks the user to enter some text, writes that text to a file, and then prompts the user for additional text to append to the same file. After writing and appending, the program opens the file again to display its final contents. It also handles the case where the file might not be found when trying to read it.

### Concepts Practiced

- Taking text input from the user  
- Opening a file in write mode (`wt`) to create/overwrite content  
- Opening a file in append mode (`at`) to add more content without erasing existing data  
- Providing feedback messages after writing and appending data  
- Opening a file in read mode (`rt`) to view its contents  
- Reading and printing lines from a text file  
- Using `try-except` to handle `FileNotFoundError` when reading  
- Reinforcing the idea of persistent storage using files  

### Expected Behavior

- The user is prompted to enter an initial line of text, which is written to a file.  
- The user is then asked for additional text, which is appended to the same file.  
- After writing and appending, the program attempts to open the file and display its contents line by line.  
- If the file exists, the final content is printed.  
- If the file does not exist, an appropriate error message is shown.
