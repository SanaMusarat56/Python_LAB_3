class AgeError(Exception):
    """Custom exception for invalid age"""
    pass

def check_age(age):
    if age < 18:
        raise AgeError("Age is below 18, access denied!")
    print("Access granted")

try:
    check_age(15)
except AgeError as e:
    print("Error:", e)