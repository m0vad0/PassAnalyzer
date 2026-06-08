#load wordlist into set
def load_wordlist():
    wordlist = set()
    with open("/usr/share/wordlists/rockyou.txt", "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            wordlist.add(line.strip())
    return wordlist

#check for obvious and sequential patterns
def has_obvious_pattern(password):
    count = 1
    seq_count = 1
    for i in range(len(password)-1):
        if password[i] == password[i + 1]:
            count += 1
            if count >= 3:
                return True
        else:
            count = 1
    #check for sequential characters     
    if ord(password[i + 1]) - ord(password[i]) == 1:
        seq_count += 1
        if seq_count >= 3:
            return True
    else:        
        seq_count = 1
    return False
    
    
#rate the strength of the password
def analyze_password(password, wordlist):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    length = len(password)
    
    #provdiding feedback on how to improve the password
    feedback = []
    if length < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not has_upper:
        feedback.append("Include at least one uppercase letter.")
    if not has_lower:
        feedback.append("Include at least one lowercase letter.")
    if not has_digit:
        feedback.append("Include at least one digit.")
    if not has_special:
        feedback.append("Include at least one special character.")
    if password in wordlist:
        feedback.append("Avoid using common passwords.")
    if has_obvious_pattern(password):
        feedback.append("Avoid obvious patterns like '1234' or 'password'.")
    
    #rate the password based on the criteria
    if length >= 12 and has_special and has_digit and has_upper and has_lower and password not in wordlist and not has_obvious_pattern(password):
        return "very strong", feedback
    elif length >= 8 and has_special and has_digit and has_upper and has_lower and password not in wordlist and not has_obvious_pattern(password):
        return "strong", feedback
    elif length >= 8 and has_upper and has_lower and has_digit and has_special and (has_obvious_pattern(password) or password in wordlist):
        return "fair", feedback
    else:
        return "weak", feedback
    
    


input_password = input("Enter a password to analyze: ")
wordlist = load_wordlist()
result, feedback = analyze_password(input_password, wordlist)
print(f"The password is: {result}")
if len(feedback) == 0:
    print("Your password looks great!.")
else:
    for item in feedback:
        print(f"- {item}")


    
