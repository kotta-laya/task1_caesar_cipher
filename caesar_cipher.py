import sys

def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def brute_force_decrypt(text):
    results = {}
    
    print("\n" + "="*60)
    print("BRUTE FORCE DECRYPTION RESULTS (All 25 shifts):")
    print("="*60)
    
    for shift in range(1, 26):
        decrypted_text = encrypt(text, -shift)
        results[shift] = decrypted_text
        print(f"Shift {shift:2d}: {decrypted_text}")
    
    print("="*60)
    return results

def display_menu():
    print("\n" + "="*50)
    print("        CAESAR CIPHER TOOL")
    print("="*50)
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Brute force decrypt (try all shifts)")
    print("4. Exit")
    print("-"*50)

def get_shift_value():
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Please enter a number between 1 and 25!")
        except ValueError:
            print("Invalid input! Please enter a valid integer!")

def save_to_file(text, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Result saved to {filename}")
        return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False

def load_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("\n--- ENCRYPTION MODE ---")
            
            print("\nHow would you like to provide the message?")
            print("1. Type the message directly")
            print("2. Load from a file")
            input_method = input("Enter choice (1 or 2): ")
            
            message = ""
            if input_method == '1':
                message = input("Enter the message to encrypt: ")
            elif input_method == '2':
                filename = input("Enter filename to load from: ")
                loaded_message = load_from_file(filename)
                if loaded_message:
                    message = loaded_message
                else:
                    continue
            else:
                print("Invalid choice!")
                continue
            
            shift = get_shift_value()
            encrypted_message = encrypt(message, shift)
            
            print("\n" + "-"*50)
            print(f"Original message: {message}")
            print(f"Shift value: {shift}")
            print(f"Encrypted message: {encrypted_message}")
            print("-"*50)
            
            save_choice = input("\nSave encrypted message to file? (y/n): ")
            if save_choice.lower() == 'y':
                filename = input("Enter filename (e.g., encrypted.txt): ")
                save_to_file(encrypted_message, filename)
        
        elif choice == '2':
            print("\n--- DECRYPTION MODE ---")
            
            print("\nHow would you like to provide the message?")
            print("1. Type the message directly")
            print("2. Load from a file")
            input_method = input("Enter choice (1 or 2): ")
            
            message = ""
            if input_method == '1':
                message = input("Enter the message to decrypt: ")
            elif input_method == '2':
                filename = input("Enter filename to load from: ")
                loaded_message = load_from_file(filename)
                if loaded_message:
                    message = loaded_message
                else:
                    continue
            else:
                print("Invalid choice!")
                continue
            
            shift = get_shift_value()
            decrypted_message = decrypt(message, shift)
            
            print("\n" + "-"*50)
            print(f"Encrypted message: {message}")
            print(f"Shift value: {shift}")
            print(f"Decrypted message: {decrypted_message}")
            print("-"*50)
            
            save_choice = input("\nSave decrypted message to file? (y/n): ")
            if save_choice.lower() == 'y':
                filename = input("Enter filename (e.g., decrypted.txt): ")
                save_to_file(decrypted_message, filename)
        
        elif choice == '3':
            print("\n--- BRUTE FORCE DECRYPTION MODE ---")
            
            print("\nHow would you like to provide the encrypted message?")
            print("1. Type the message directly")
            print("2. Load from a file")
            input_method = input("Enter choice (1 or 2): ")
            
            message = ""
            if input_method == '1':
                message = input("Enter the encrypted message to brute force: ")
            elif input_method == '2':
                filename = input("Enter filename to load from: ")
                loaded_message = load_from_file(filename)
                if loaded_message:
                    message = loaded_message
                else:
                    continue
            else:
                print("Invalid choice!")
                continue
            
            results = brute_force_decrypt(message)
            
            save_choice = input("\nSave all brute force results to file? (y/n): ")
            if save_choice.lower() == 'y':
                filename = input("Enter filename (e.g., brute_force_results.txt): ")
                formatted_results = f"BRUTE FORCE DECRYPTION RESULTS\n{'='*40}\nOriginal encrypted text: {message}\n\n"
                for shift, text in results.items():
                    formatted_results += f"Shift {shift:2d}: {text}\n"
                
                save_to_file(formatted_results, filename)
        
        elif choice == '4':
            print("\nThank you for using the Caesar Cipher Tool!")
            print("Goodbye!")
            sys.exit()
        
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")
        
        print("\n" + "-"*50)
        continue_choice = input("Do you want to perform another operation? (y/n): ")
        if continue_choice.lower() != 'y':
            print("\nThank you for using the Caesar Cipher Tool!")
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()