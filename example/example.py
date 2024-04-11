import requests
from utils.utils import *

url = "https://httpbin.org/anything/{anything}"

headers = {"Hello": "there"}

payload = {}

response = requests.post(url, headers = headers, data=payload)

print_detailed_response(response)