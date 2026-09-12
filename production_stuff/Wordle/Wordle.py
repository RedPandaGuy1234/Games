import warnings
warnings.filterwarnings('ignore', message='urllib3 v2 only supports OpenSSL')
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

txt_url = "https://raw.githubusercontent.com/RedPandaGuy1234/Games/refs/heads/main/production_stuff/Wordle/Valid_Words.txt"
response = requests.get(txt_url)

if response.status_code == 200:
    Valid_Words = response.text.splitlines()
else:
    Valid_Words = []
    print("This code has failed because the list for valid words did not show up. Please alert RedPandaGuy1234 of this. Thank you!")
    sys.exit(1)

txt_url = "https://raw.githubusercontent.com/RedPandaGuy1234/Games/refs/heads/main/production_stuff/Wordle/Word_Bank.txt"
response = requests.get(txt_url)

if response.status_code == 200:
    Word_bank = response.text.splitlines()
else:
    Word_bank = []
    print("This code has failed because the list for the word bank did not show up. Please alert RedPandaGuy1234 of this. Thank you!")
    sys.exit(1)
