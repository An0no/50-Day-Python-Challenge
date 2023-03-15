import random
import string

def generate_password(length):
    # define all possible characters for password generation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # randomly select characters from the character set and join them into a string
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password
password = generate_password(12)
print(password)
