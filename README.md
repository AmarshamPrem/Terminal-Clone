# Terminal Stock Investment Game

A Python-based terminal game designed to teach basic concepts of stock market investment in a safe, simulated environment. This project serves as both a learning tool for Python programming and a simple introduction to stock market mechanics.

## 🎯 Purpose and Educational Goals

This project was created with the following learning objectives in mind:

1. **Programming Concepts**
   - File I/O operations with JSON
   - Command-line interface design
   - User authentication system
   - State management
   - Error handling
   - Data persistence

2. **Stock Market Concepts**
   - Basic investment mechanics
   - Stock performance tracking
   - Risk management with virtual money
   - Portfolio management

## 🚀 Features

- **User Authentication System**
  - Create new user accounts
  - Secure login with username/password
  - Persistent user data storage

- **Virtual Stock Market**
  - 6 different stocks (A through F)
  - Random performance fluctuations (-100% to +100%)
  - Real-time investment simulation

- **Command System**
  - Interactive terminal interface
  - Comprehensive command set
  - Built-in help and syntax guide

## 📝 Available Commands

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

4. `syntax` - Get help with commands
   - Syntax: `syntax <command_name>`
   - Example: `syntax invest`

5. `list` - Show all available commands

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

## 🔧 File Structure

- `gameTerminal.py` - Main game file containing all logic
- `user.json` - User data storage file
- `README.md` - Documentation and guide (this file)

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
