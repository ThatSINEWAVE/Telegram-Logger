from datetime import datetime
import subprocess


def send_telegram_message(log_message):
    try:
        command = [
            'curl',
            '-X', 'POST',
            'https://api.telegram.org/(YOUR_BOT_KEY)/sendMessage',
            '-d', f'chat_id=-(YOUR_CHAT_ID)&text={log_message}'
        ]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        with open('error_log.txt', 'a') as f:
            f.write(str(e) + '\n')


def custom_print(*args, **kwargs):
    original_print(*args, **kwargs)

    message = " ".join(map(str, args))
    send_telegram_message(message)


original_print = print
print = custom_print


def get_formatted_date_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S on %d.%m.%Y")


def startup(browser, code):
    print(f"APP HAS STARTED RUNNING AT {get_formatted_date_time()}")


def shutdown():
    print(f"APP IS QUITTING AT {get_formatted_date_time()}")


# For testing purposes, calling the startup function with dummy arguments
startup(None, None)

try:
    while True:
        # The script will keep running indefinitely, listening to the print statements or any other triggers you set up
        pass
except KeyboardInterrupt:
    # Handle other exceptions if needed
    pass
finally:
    # This block will execute when the script is interrupted, calling the shutdown function
    shutdown()
