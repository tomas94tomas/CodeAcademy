import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Today's BBC Headlines:")

headlines = soup.find_all("h3")
print(f"Found {len(headlines)} h3 tags")

for headline in headlines[:10]:
    print(headline.text.strip())