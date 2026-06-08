# PassAnalyzer
A simple Password analyzer tool built with Python that evaluates a password strength by checking for common weaknesses and obvious patterns. This helps user understand how secure their password is and provides feedback

# FEATURES
- Checks password length

- Detects uppercase and lowercase characters

- Detects numbers and special characters

- Identifies common patterns (e.g., sequential numbers, repeated characters)

- Rates password strength by (fair, weak, strong and very strong)

# Example
Enter a password to analyze: pass


The password is: weak

- Password should be at least 8 characters long.

- Include at least one uppercase letter.

- Include at least one digit.

- Include at least one special character.

- Avoid using common passwords.

Enter a password to analyze: Password1!  
The password is: fair  
- Avoid using common passwords.

# REQUIREMENTS
Before running PassAnalyzer, ensure you have:  
- Kali Linux
- Python 3.13.12
- the RockYou wordlist located at:

/usr/share/wordlists/rockyou.txt

# INSTALLATION

1. Clone the repository:  
   git clone https://github.com/m0vad0/PassAnalyzer.git
2. Verify that Python 3.13.12 is installed  
   python3 --version
3. Verify RockYou wordlist exists:  
   ls /usr/share/wordlists/rockyou.txt
4. Run the analyzer:  
   python3 password_analyzer.py

  
# HOW IT WORKS
The analyzer evaluates passwowrds using several criteria:  
- Length
- Character diversity
- Repeated patterns
- Sequential characters
- Common password indicators

Based on these checks, it generates a strength rating and feedback.  

# FUTURE IMPROVEMENTS
- Password entropy calculation
- Dictionary attack simulation
- Password breach database integration
- Graphical User Interface
- Password generation feature

# TECHNOLOGIES USED
- pythhon 3
  
