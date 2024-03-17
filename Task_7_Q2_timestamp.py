
# file Handling to read a text file & displays its content to the console
def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            print("Content of", file_name, ":\n", file_content)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)

# Example
file_name = input("Enter the name of the text file to read: ")
read_text_file(file_name)

