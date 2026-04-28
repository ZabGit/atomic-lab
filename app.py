import requests

def validate_email(email):
    if "@" not in email:
        return False
    return True

def get_user_status(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}/status")
    return response.json()["status"]

def main():
    email = "test@example.com"
    if validate_email(email):
        print(f"Email {email} is valid")
    
    status = get_user_status(123)
    print(f"User status: {status}")

if __name__ == "__main__":
    main()