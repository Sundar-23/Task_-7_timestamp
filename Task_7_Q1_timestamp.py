
# Program for create current timestamp:
from datetime import datetime


def create_text_file_with_timestamp():
    # Generate timestamp
    current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # file creating timestamp as filename
    file_name = f"text_file_{current_timestamp}.txt"

    # Write timestamp into file
    with open(file_name, 'w') as file:
        file.write(current_timestamp)

    print(f"Text file '{file_name}' created with the current timestamp.")


# Call the function to create the text file
create_text_file_with_timestamp()
