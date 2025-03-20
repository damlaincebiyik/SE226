import random
import string

def get_replacements():
    letters_dict = {}
    all_replacements = set()
    
    for i in range(5):
        while True:
            letter = input("Enter a lowercase character: ")
            if len(letter) != 1 or not letter.islower() or letter in letters_dict:
                print("Please enter a single lowercase letter that hasn't been used before.")
                continue
            
            replacements = set()
            for j in range(3):
                while True:
                    replacement = input(f"Enter a replacement for '{letter}': ")
                    if len(replacement) != 1:
                        print("Please enter a single character.")
                    elif replacement in all_replacements:
                        print("This replacement character is already used for another letter.")
                    else:
                        replacements.add(replacement)
                        all_replacements.add(replacement)
                        break
            
            letters_dict[letter] = list(replacements)
            break
    
    return letters_dict

def generate_passwords(letters_dict):
    passwords = []
    for _ in range(5):
        password = ''.join(random.choices(string.ascii_lowercase, k=15))
        passwords.append(password)
    
    modified_passwords = []
    for password in passwords:
        modified = list(password)
        for i, char in enumerate(modified):
            if char in letters_dict:
                modified[i] = random.choice(letters_dict[char])
        modified_passwords.append(''.join(modified))
    
    return passwords, modified_passwords

def categorize_passwords(original_passwords, modified_passwords, letters_dict):
    categorized_passwords = {"strong": [], "weak": []}
    
    for original, modified in zip(original_passwords, modified_passwords):
        replacement_count = 0
        for orig_char, mod_char in zip(original, modified):
            if orig_char in letters_dict and mod_char != orig_char:
                replacement_count += 1
        
        if replacement_count > 4:
            categorized_passwords["strong"].append(modified)
        else:
            categorized_passwords["weak"].append(modified)
    
    return categorized_passwords

letters_dict = get_replacements()

original_passwords, modified_passwords = generate_passwords(letters_dict)
categorized = categorize_passwords(original_passwords, modified_passwords, letters_dict)

print("\nGenerated Passwords:")
print("STRONG PASSWORDS:")
for password in categorized["strong"]:
    print(password)

print("WEAK PASSWORDS:")
for password in categorized["weak"]:
    print(password)