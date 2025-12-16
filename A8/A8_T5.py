import auth_lib

def main() -> None:
    """Main program for login and register system."""
    print("Program starting.")
    
    current_user = None  # [id, username, password_hash] or None if not logged in
    
    while True:
        if current_user is None:
            # Main menu (not logged in)
            show_main_menu()
            choice = ask_choice()
            
            if choice == 0:
                print("Exiting program.\n")
                break
            elif choice == 1:
                # Login
                username = input("Insert username: ")
                password = input("Insert password: ")
                success, user_data = auth_lib.login_user(username, password)
                if success:
                    current_user = user_data
            elif choice == 2:
                # Register
                username = input("Insert username: ")
                password = input("Insert password: ")
                auth_lib.register_user(username, password)
            else:
                print("Unknown option!\n")
                
        else:
            # User menu (logged in)
            show_user_menu(current_user[1])
            choice = ask_choice()
            
            if choice == 0:
                # Logout
                print("Logging out...\n")
                current_user = None
            elif choice == 1:
                # View profile
                print(f"\nUser Profile:")
                print(f"ID: {current_user[0]}")
                print(f"Username: {current_user[1]}")
                print(f"Password Hash: {current_user[2]}\n")
            elif choice == 2:
                # Change password
                old_pass = input("Insert old password: ")
                new_pass = input("Insert new password: ")
                confirm_pass = input("Confirm new password: ")
                
                if new_pass != confirm_pass:
                    print("New passwords don't match!\n")
                else:
                    auth_lib.change_password(current_user[1], old_pass, new_pass)
                    # Update current user data
                    credentials = auth_lib.read_credentials()
                    for cred in credentials:
                        if cred[1] == current_user[1]:
                            current_user = cred
                            break
            else:
                print("Unknown option!\n")
    
    print("Program ending.")

def show_main_menu() -> None:
    """Display main menu (not logged in)."""
    print("\nOptions:")
    print("1 - Login")
    print("2 - Register")
    print("0 - Exit")

def show_user_menu(username: str) -> None:
    """Display user menu (logged in)."""
    print(f"\nWelcome, {username}!")
    print("Options:")
    print("1 - View profile")
    print("2 - Change password")
    print("0 - Logout")

def ask_choice() -> int:
    """Get user choice and return as integer."""
    user_input = input("Your choice: ")
    if user_input.isnumeric():
        return int(user_input)
    else:
        print("Unknown option!")
        return -1

main()