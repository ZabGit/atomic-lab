import requests

def validate_email_address(email):
    if "@" not in email or "." not in email:
        return False
    return True

def get_user_current_status(user_id):
    try:
        response = requests.get(f"https://api.example.com/users/{user_id}/status")
        response.raise_for_status()
        return response.json()["status"]
    except requests.exceptions.RequestException:
        return "unknown"

def check_user_active_status(user_id):
    status = get_user_current_status(user_id)
    return status == "active"

def main():
    email = "test@example.com"
    if validate_email_address(email):
        print(f"Email {email} is valid")
    
    user_id = 123
    status = get_user_current_status(user_id)
    print(f"User status: {status}")
    
    is_active = check_user_active_status(user_id)
    print(f"Is user active: {is_active}")

if __name__ == "__main__":
    main()