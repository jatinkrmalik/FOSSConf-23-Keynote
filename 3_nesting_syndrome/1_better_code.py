def process_user_data(user_data):
    if user_data is None:
        # do something else as well!
        return "No user data provided."
    if 'name' not in user_data:
        return "Name is missing."
    if 'age' not in user_data:
        return "Age is missing."
    if user_data['age'] <= 18:
        return "User is underage."
    if 'email' not in user_data:
        return "Email is missing."
    if not user_data['email'].endswith('@example.com'):
        return "Invalid email domain."
    if 'address' not in user_data:
        return "Address is missing."
    if 'city' not in user_data['address']:
        return "City is missing."

    # Main processing logic after all validations
    return "User data is valid."

def test_process_user_data():
    # Test success path
    user_data_valid = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'address': {'city': 'Wonderland'}}
    assert process_user_data(user_data_valid) == "User data is valid."

    # Test error path
    user_data_invalid = {'name': 'Bob', 'age': 17, 'email': 'bob@example.com'}
    assert process_user_data(user_data_invalid) == "User is underage."

test_process_user_data()
