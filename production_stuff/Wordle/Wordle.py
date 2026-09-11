import Valid_Words.txt

# Change this to the actual raw file later, once this is finished.

txt_url = "https://raw.githubusercontent.com/RedPandaGuy1234/Games/refs/heads/main/production_stuff/Wordle/Valid_Words.txt"
response = requests.get(txt_url)

if response.status_code == 200:
    Valid_Words = response.text.splitlines()
else:
    Valid_Words = []

# This is a test to see if it works, will be deleted later.
print(Valid_Words)
