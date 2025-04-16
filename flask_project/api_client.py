import requests
import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")

def get_users():
    response = requests.get(f"{BASE_URL}/users")
    return response.json()

def get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    return response.json()

def add_user(name, email):
    data = {"name": name, "email": email}
    response = requests.post(f"{BASE_URL}/users", json=data)
    return response.json()

if __name__ == "__main__":
    print("Visi vartotojai:", get_users())
    print("Vartotojas ID 1:", get_user(1))
    new_user = add_user("Mantas", "mantas@example.com")
    print("Pridėtas vartotojas:", new_user)
    print("Atnaujintas vartotojų sąrašas:", get_users())
