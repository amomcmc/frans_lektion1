import os

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.readlines()
            for line in content:
                print(line.strip())
    else:
        print("The file doesnt exist")
        
def create_file(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            print(f"File was created: {filename}")
    else:
        print(f"File already exists: {filename}")
        
while True:
    print("Menu:")
    print("1. Read a file")
    print("2. Create a file")
    print("3. Append to file")
    print("4. Erase file")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        filename = input("Select file: ")
        read_file(filename)
    elif choice == '2':
        filename = input("Enter filename: ")
        create_file(filename)