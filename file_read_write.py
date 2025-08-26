# file_read_write.py

def file_read_write():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, "r") as f:
            content = f.read()

        modified_content = content.upper()

        output_file = "output.txt"
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Success! Modified content written to '{output_file}'")

    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    file_read_write()
