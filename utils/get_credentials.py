def edit_credentials():
    name, email, password = get_credentials()
    name += '1'
    email_parts = email.split('@')
    email = email_parts[0] + '1' + email_parts[1]
    print(f'test {email}')
    password += '1'

    with open('credentials.txt', 'w') as file:
        file.write(f'{name},{email},{password}')


def get_credentials():
    try:
        with open('credentials.txt', 'r') as file:
            text = file.read()
            print(text)
            credentials = text.split(',')
            print(credentials)
            return tuple(credentials)
    except Exception as e:
        print(e)


get_credentials()