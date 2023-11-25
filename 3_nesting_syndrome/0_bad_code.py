def process_user_data(user_data):
    if user_data is not None:
        if 'name' in user_data:
            if 'age' in user_data:
                if user_data['age'] > 18:
                    if 'email' in user_data:
                        if user_data['email'].endswith('@example.com'):
                            if 'address' in user_data:
                                if 'city' in user_data['address']:
                                    # Further nested logic...
                                    return "User data is valid." 
                                else:
                                    return "City is missing."
                            else:
                                return "Address is missing."
                        else:
                            return "Invalid email domain."
                    else:
                        return "Email is missing."
                else:
                    return "User is underage."
            else:
                return "Age is missing."
        else:
            return "Name is missing."
    else:
        return "No user data provided."

def test_process_user_data():
    # Test success path
    user_data_valid = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'address': {'city': 'Wonderland'}}
    assert process_user_data(user_data_valid) == "User data is valid."
    print("Success path test passed.")

    # Test error path
    user_data_invalid = {'name': 'Bob', 'age': 17, 'email': 'bob@example.com'}
    assert process_user_data(user_data_invalid) == "User is underage."
    print("Error path test passed.")

test_process_user_data()
