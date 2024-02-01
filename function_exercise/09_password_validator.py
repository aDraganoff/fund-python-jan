def check_password(password):
    count_digits = 0
    for _ in range(len(password)):
        if password[_].isnumeric():
            count_digits += 1

    if 6 <= len(password) <=10:
        if password.isalnum():
            if count_digits >= 2:
                return "Password is valid"
            else:
                return "Password must have at least 2 digits"
        else:
            return "Password must consist only of letters and digits"
    else:
        return "Password must be between 6 and 10 characters"


password = input()
result = check_password(password)
print(result)
