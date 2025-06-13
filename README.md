# Terminal Stock Investment Game with File Management

A Python-based terminal application that combines stock market investment simulation with powerful file management capabilities. This project serves as both a learning tool for Python programming and provides practical file management utilities.

## 🎯 Purpose and Educational Goals

This project was created with the following learning objectives in mind:

1. **Programming Concepts**
   - File I/O operations with JSON
   - Command-line interface design
   - User authentication system
   - State management
   - Error handling
   - Data persistence
   - Multi-language file execution
   - Text file manipulation

2. **Stock Market Concepts**
   - Basic investment mechanics
   - Stock performance tracking
   - Risk management with virtual money
   - Portfolio management

## 🚀 Features

### Investment Game Features
- **User Authentication System**
  - Create new user accounts
  - Secure login with username/password
  - Persistent user data storage

- **Virtual Stock Market**
  - 6 different stocks (A through F)
  - Random performance fluctuations (-100% to +100%)
  - Real-time investment simulation

### File Management Features
- **File Operations**
  - Read text files
  - Create and edit files
  - Save files to custom locations
  - Execute code files in multiple languages

- **Command System**
  - Interactive terminal interface
  - Comprehensive command set
  - Built-in help and syntax guide

## 📝 Available Commands

### Investment Commands
1. `get` - Retrieve information
   - `get username` - Display current username
   - `get password` - Display current password
   - `get money` - Check current balance
   - `get stin` - Get current stock information
   - `get all` - Display all user information

2. `set` - Modify user information
   - `set username <new_username>` - Change username
   - `set password <new_password>` - Change password

3. `invest` - Make stock investments
   - Syntax: `invest <amount> <stock>`
   - Example: `invest 100 a`

### File Management Commands

4. `read` - Read text files
   - Syntax: `read <filepath>`
   - Example: `read document.txt`
   - Supported extensions: .txt, .py, .js, .html, .css, .json, .md, .csv, .log, .xml, .yml, .yaml, .ini, .cfg

5. `write` - Create new text files
   - Syntax: `write <filename> <extension>`
   - Example: `write myfile txt`
   - Type 'END' on a new line to finish writing
   - Supports same extensions as read command

6. `save` - Save written files
   - Syntax: `save <folder_path>`
   - Example: `save C:\Documents\MyFiles`
   - Creates folders if they don't exist

7. `execute` - Run code files
   - Syntax: `execute <filepath>`
   - Example: `execute script.py`
   - Supported languages and required tools:
     - Python (.py) - Python interpreter
     - JavaScript (.js) - Node.js
     - Java (.java) - JDK
     - C++ (.cpp) - G++ compiler
     - C (.c) - GCC compiler
     - Ruby (.rb) - Ruby interpreter
     - PHP (.php) - PHP interpreter
     - Perl (.pl) - Perl interpreter
     - Shell Scripts (.sh) - Bash
     - PowerShell Scripts (.ps1) - PowerShell

8. `syntax` - Get help with commands
   - Syntax: `syntax <command_name>`
   - Example: `syntax execute`

9. `list` - Show all available commands

## 🎮 How to Play

1. **Starting the Game**
   ```bash
   python gameTerminal.py
   ```

2. **First-time Setup**
   - Enter a username and password when prompted
   - You'll start with $1000 in virtual money

3. **Basic Gameplay Loop**
   1. Use `get stin` to check current stock performances
   2. Analyze which stocks are performing well
   3. Use `invest` command to buy stocks
   4. Monitor your money using `get money`

4. **Investment Strategy**
   - Stocks perform randomly between -100% and +100%
   - Positive performance means profit
   - Negative performance means loss
   - Start with small investments to learn the system

## 💡 Learning Tips

1. **Start Small**
   - Begin with small investments
   - Try investing $100 in different stocks
   - Compare results to understand the random nature of returns

2. **Track Your Progress**
   - Keep notes of which stocks perform well
   - Record your starting and ending amounts
   - Try to develop investment strategies

3. **Experiment Safely**
   - Try different investment amounts
   - Test various combinations of stocks
   - Learn from losses without real financial risk

## 🛠️ Technical Implementation

The game uses:
- Python's built-in `json` module for data persistence
- Random number generation for stock performance
- File I/O for saving user data
- Command pattern for handling user input
- Dictionary-based command documentation

## 🛠️ Technical Requirements

1. **Base Requirements**
   - Python 3.x
   - JSON module (built-in)

2. **For Code Execution Features**
   - Python interpreter
   - Node.js for JavaScript
   - JDK for Java
   - G++ compiler for C++
   - GCC compiler for C
   - Ruby interpreter
   - PHP interpreter
   - Perl interpreter
   - Bash shell
   - PowerShell

## 🔧 File Structure

- `gameTerminal.py` - Main application file containing all logic
- `user.json` - User data storage file
- `README.md` - Documentation and guide (this file)
- Created files - Stored in user-specified locations

## 🎓 Educational Exercise Ideas

1. **Code Study**
   - Review the JSON file handling
   - Understand the command processing system
   - Study the error handling implementation

2. **Possible Enhancements**
   - Add historical tracking of investments
   - Implement more complex stock behavior
   - Add market trends and sectors
   - Create a graphical interface

## 🤝 Contributing

This is an educational project, and suggestions for improvements are welcome! Some areas that could be enhanced:
- More realistic stock market simulation
- Additional commands and features
- Better error handling
- User interface improvements

## 📝 License

This project is open-source and available for educational purposes. Feel free to use, modify, and learn from it!
