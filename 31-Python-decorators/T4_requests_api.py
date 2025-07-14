import requests

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke = response.json()
    print(f"{joke['setup']} ... {joke['punchline']}")

if __name__ == "__main__":
    fetch_joke()
