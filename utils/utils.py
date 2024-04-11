import json
import subprocess
import base64
import os

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
PINK = '\033[38;5;204m'
ORANGE = '\033[38;5;214m'
RESET = '\033[0m'  # Reset to default color

def b64encode(string):
    encoded_bytes = base64.b64encode(string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def b64decode(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    return decoded_bytes.decode('utf-8')

def get_basic_auth_str(username, password):
    username_password = f"{username}:{password}"
    return f"Basic {b64encode(username_password)}"

def clear_terminal():
    if os.system == 'nt':
        subprocess.run(['cls'], shell=True)
    else:
        subprocess.run(['clear'], shell=True)

def print_with_color(strings, color=RESET):
    combined_string = ''.join(map(str, str(strings)))
    print(f"{color}{combined_string}{RESET}")

def print_detailed_response(response):
    clear_terminal()
    print("--------------------------------------------------------------------")
    print("Status Code: ", end="")
    print_with_color(response.status_code, color=YELLOW)
    print()
    print("Headers")
    print_with_color(response.headers, color=PINK)
    print()
    print("Response Body:")
    print_with_color(response.text, color=ORANGE)
    print()
    print("Elapsed Time:", response.elapsed)  # Time taken for the request
    print("URL:", response.url)  # URL that was hit
    print("--------------------------------------------------------------------")