import hashlib

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def hash_password(password: str) -> str:
    """Hash password using MD5 and return hex string."""
    return hashlib.md5(password.encode()).hexdigest()

def read_credentials() -> list[list[str]]:
    """Read all credentials from file."""
    credentials = []
    try:
        with open(CREDENTIALS_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(DELIMITER)
                    if len(parts) == 3:  # id;username;password_hash
                        credentials.append(parts)
        return credentials
    except FileNotFoundError:
        # Create empty file if it doesn't exist
        with open(CREDENTIALS_FILE, 'w') as file:
            pass
        return []

def write_credentials(credentials: list[list[str]]) -> None:
    """Write all credentials to file."""
    with open(CREDENTIALS_FILE, 'w') as file:
        for cred in credentials:
            file.write(f"{cred[0]}{DELIMITER}{cred[1]}{DELIMITER}{cred[2]}\n")

def get_next_id(credentials: list[list[str]]) -> int:
    """Get next available ID for new user."""
    if not credentials:
        return 1
    return max(int(cred[0]) for cred in credentials) + 1

def register_user(username: str, password: str) -> bool:
    """Register a new user."""
    credentials = read_credentials()
    
    # Check if username already exists (optional)
    for cred in credentials:
        if cred[1] == username:
            print("Username already exists!")
            return False
    
    # Create new user
    user_id = get_next_id(credentials)
    password_hash = hash_password(password)
    
    credentials.append([str(user_id), username, password_hash])
    write_credentials(credentials)
    
    print("User registration completed!")
    return True

def login_user(username: str, password: str) -> tuple[bool, list[str]]:
    """Attempt to login a user."""
    credentials = read_credentials()
    password_hash = hash_password(password)
    
    for cred in credentials:
        if cred[1] == username and cred[2] == password_hash:
            print("Login successful!")
            return True, cred
    
    print("Invalid username or password!")
    return False, []

def change_password(username: str, old_password: str, new_password: str) -> bool:
    """Change user's password."""
    credentials = read_credentials()
    
    for i, cred in enumerate(credentials):
        if cred[1] == username and cred[2] == hash_password(old_password):
            credentials[i][2] = hash_password(new_password)
            write_credentials(credentials)
            print("Password changed successfully!")
            return True
    
    print("Invalid credentials!")
    return False