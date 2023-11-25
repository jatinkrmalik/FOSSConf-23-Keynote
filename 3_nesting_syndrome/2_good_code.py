def validate_user_data(user_data):
    if user_data is None:
        raise ValueError("No user data provided.")
    if 'name' not in user_data:
        raise ValueError("Name is missing.")
    if 'age' not in user_data:
        raise ValueError("Age is missing.")
    if user_data['age'] <= 18:
        raise ValueError("User is underage.")
    if 'email' not in user_data:
        raise ValueError("Email is missing.")
    if not user_data['email'].endswith('@example.com'):
        raise ValueError("Invalid email domain.")
    if 'address' not in user_data:
        raise ValueError("Address is missing.")
    if 'city' not in user_data['address']:
        raise ValueError("City is missing.")

def process_user_data(user_data):
    try:
        validate_user_data(user_data)
        return "User data is valid."
    except ValueError as error:
        return str(error)

def test_process_user_data():
    # Test success path
    user_data_valid = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'address': {'city': 'Wonderland'}}
    assert process_user_data(user_data_valid) == "User data is valid."

    # Test error path
    user_data_invalid = {'name': 'Bob', 'age': 17, 'email': 'bob@example.com'}
    assert process_user_data(user_data_invalid) == "User is underage."

test_process_user_data()
