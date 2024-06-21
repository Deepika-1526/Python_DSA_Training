password = "A1234a@4"


has_lowercase = False
has_uppercase = False
has_special = False

missing_count = 0

special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"


if len(password) <= 8:

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char in special_characters:
            has_special = True

    if not has_lowercase:
        missing_count += 1
    if not has_uppercase:
        missing_count += 1
    if not has_special:
        missing_count += 1
else:
    missing_count = 1  

print(missing_count)

