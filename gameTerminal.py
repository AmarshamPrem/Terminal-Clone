import json, random
import os

# Initialize default user data
userData = {
    "username": "",
    "password": "",
    "money": 1000
}

# Global variables for file handling
current_file = []
current_filename = None

try:
    if os.path.exists("user.json") and os.path.getsize("user.json") > 0:
        with open("user.json", "r") as file:
            userData = json.load(file)
    else:
        with open("user.json", "w") as file:
            json.dump(userData, file)

    print("\n\t\tWelcome to the Investment In Stocks Game\n")
    print("Please Enter Your Details.")
    username = input("Please enter your Username: ")
    password = input("Please enter your Password: ")
    
    if userData["username"] == "" and userData["password"] == "":
        userData.update({
            "username": username,
            "password": password,
            "money": 1000
        })
        with open("user.json", "w") as f:
            json.dump(userData, f)
        print("Successfully created new account")
    elif userData["username"] != username or userData["password"] != password:
        print("Invalid Username or Password")
        quit()
    else:
        print("Successfully Logged In")

except Exception as e:
    print(f"Error accessing user data: {str(e)}")
    quit()

def emptyList(item):
    if item == "":
        return False
    else: return True

def processCmd(cmd, ud, data=None):
    global lastData
    global current_file
    global current_filename
    if cmd == "exit":
        exit()

    elif cmd.startswith("write"):
        l = cmd.split(" ")
        l = list(filter(emptyList, l))
        if len(l) != 3:
            print("Invalid command. Usage: write <filename> <extension>")
            return
            
        filename = l[1]
        extension = l[2] if l[2].startswith('.') else '.' + l[2]
        
        # List of allowed text file extensions
        text_extensions = ['.txt', '.py', '.js', '.html', '.css', '.json', '.md', '.csv', '.log', '.xml', '.yml', '.yaml', '.ini', '.cfg']
        
        if extension not in text_extensions:
            print(f"Error: Cannot create this file type. Allowed extensions are: {', '.join(text_extensions)}")
            return
            
        # Store the current file and filename for later saving
        global current_file
        global current_filename
        current_filename = filename + extension
        current_file = []
        
        print(f"Creating new file: {current_filename}")
        print("Enter your content (type '$END$/' on a new line to finish):")
        
        while True:
            line = input()
            if line.strip() == '$END$':
                break
            current_file.append(line)
            
        print(f"Content stored in memory. Use 'save <folder_path>' to save the file.")

    elif cmd.startswith("save"):
        if not current_file:
            print("No content to save. Use 'write' command first to create content.")
            return
            
        l = cmd.split(" ")
        l = list(filter(emptyList, l))
        if len(l) != 2:
            print("Invalid command. Usage: save <folder_path>")
            return
            
        folder_path = l[1]
        
        # Create folder if it doesn't exist
        try:
            os.makedirs(folder_path, exist_ok=True)
            file_path = os.path.join(folder_path, current_filename)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(current_file))
            
            print(f"File successfully saved as: {file_path}")
            # Reset the current file
            current_file = []
            current_filename = None
            
        except Exception as e:
            print(f"Error saving file: {str(e)}")
            return

    elif cmd.startswith("read"):
        l = cmd.split(" ")
        l = list(filter(emptyList, l))
        if len(l) != 2:
            print("Invalid command. Usage: read <filepath>")
            return
        
        filepath = l[1]
        # Check if file exists
        if not os.path.exists(filepath):
            print(f"Error: File '{filepath}' does not exist")
            return
            
        # List of text file extensions we'll allow
        text_extensions = ['.txt', '.py', '.js', '.html', '.css', '.json', '.md', '.csv', '.log', '.xml', '.yml', '.yaml', '.ini', '.cfg']
        file_ext = os.path.splitext(filepath)[1].lower()
        
        if file_ext not in text_extensions:
            print(f"Error: Cannot read this file type. Allowed extensions are: {', '.join(text_extensions)}")
            return
            
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                print(f"\nReading file: {filepath}\n{'-' * 40}")
                for line_number, line in enumerate(file, 1):
                    print(f"{line_number}: {line.rstrip()}")
                print('-' * 40)
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return

    elif cmd.startswith("get"):
        l = cmd.split(" ")
        l = list(filter(emptyList, l))
        if len(l) != 2:
            print("Invalid command")
            return
        if l[1] == "username":
            print(f'Your username is \"{ud["username"]}\". To set new username use command "set".')
            return
        if l[1] == "password":
            print(f'Your password is \"{ud["password"]}\". To set new password use command "set".')
            return
        if l[1] == "money":
            print(f'Your money is \"${ud["money"]}\". To invest money in stocks use command "invest".')
            return
        if l[1] == "stin":
            data = [random.randint(-100, 100) for _ in range(6)]
            lastData = data
            print("You have $" + str(ud["money"]) + ".")
            for ind in range(0, 6):
                print("The stock " + str(stocks[ind]) + " has performed " + str(data[ind]))
            return
        if l[1] == "all":
            print(f"Your username is {ud['username']}. Your password is {ud['password']}. You have ${ud['money']}.")
            return
        else:
            print("Invalid command")
            return

    elif cmd.startswith("set"):
        l = cmd.split(" ")
        l = list(filter(emptyList, l))
        if len(l) != 3:
            print("Invalid command")
            return
        if l[1] == "username":
            ud["username"] = l[2]
        if l[1] == "password":
            ud["password"] = l[2]

        with open("user.json", "w") as f:
            json.dump(userData, f)

    elif cmd.startswith("syntax"):
        l = cmd.split(" ")
        l = list(filter(emptyList, l))
        if len(l) != 2:
            print("Invalid command")
            return
        syntax = {
            "get": {
                "use": "To retrieve something such as username.",
                "syntax": "get <var>"
            },
            "set": {
                "use": "To save something.",
                "syntax": "set <var> <value>"
            },
            "syntax": {
                "use": "Help for assholes.",
                "syntax": "syntax <cmd_name>"
            },
            "list": {
                "use": "To get all the commands.",
                "syntax": "list"
            },
            "read": {
                "use": "To read data from a file.",
                "syntax": "read <path>"
            },
            "write": {
                "use": "To write data to a file.",
                "syntax": "write <filename> <extension>"
            },
            "execute": {
                "use": "To execute code from a file.",
                "syntax": "execute <filepath> <filetype>"
            },
            "save": {
                "use": "To save a file.",
                "syntax": "save <filepath> <filename>"
            },
            "invest": {
                "use": "To invest money in stocks.",
                "syntax": "invest <money> <stock>"
            }
        }
        if l[1] in commands:
            print("Command name: " + l[1])
            print("Use Case: " + syntax[l[1]]["use"])
            print("Syntax: " + syntax[l[1]]["syntax"])
        else:
            print(f"The command {l[1]} does not exist.")
            return

    elif cmd.startswith("invest"):
        if lastData is None:
            print("Please use 'get stin' first to get current stock information")
            return
            
        l = cmd.split(" ")
        l = list(filter(emptyList, l))
        if len(l) != 3:
            print("Invalid command")
            return
        try:
            amount = int(l[1])
            stock = l[2]
            if stock not in stocks:
                print(f"Invalid stock. Available stocks are: {', '.join(stocks)}")
                return
            if amount <= 0:
                print("Amount must be positive")
                return
            if amount > ud["money"]:
                print(f"Insufficient funds. You have ${ud['money']}")
                return
                
            ind = stocks.index(stock)
            ud["money"] -= amount
            share = (amount * lastData[ind]) / 100
            ud["money"] += share + amount   
            print(f"You invested ${amount} and got back ${amount + share:.2f}")
            with open("user.json", "w") as f:
                json.dump(ud, f)
        except ValueError:
            print("Invalid amount. Please enter a number")
            return

    elif cmd.strip() == "list":
        for c in commands:
            print(c)




    else:
        print("Invalid command")
    json.dump(userData, open("user.json", "w"))
    return

commands = ["get", "set", "syntax", "list", "read", "write", "save", "invest", "execute"]
stocks = ["a", "b", "c", "d", "e", "f"]
lastData = None
i = 1

while True:
    if i == 1:
        print("\tWelcome to the Terminal. \nTo list every command use \"list\". \nTo get syntax of a particular command use \"syntax <cmd_name>\"")
        i = 2
    command = input(f"\n{username.capitalize()} %  ")
    processCmd(command, userData)
