import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///headlines.db')
Session = sessionmaker(bind=engine)

class Headline(Base):
    __tablename__ = 'headlines'
    id = Column(Integer, primary_key=True)
    site = Column(String)
    title = Column(String)

Base.metadata.create_all(engine)

def scrape_bbc():
    url = "https://www.bbc.com/news"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    headlines = []
    for h in soup.select("h2, h3"):
        text = h.get_text(strip=True)
        if text and len(text) > 10:  # crude filter for meaningful headlines
            headlines.append(text)
    return headlines

def scrape_reuters():
    url = "https://www.reuters.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    headlines = []
    for h in soup.select("h2, h3"):
        text = h.get_text(strip=True)
        if text and len(text) > 10:
            headlines.append(text)
    return headlines

def save_headlines(site, headlines):
    session = Session()
    for title in headlines:
        headline = Headline(site=site, title=title)
        session.add(headline)
    session.commit()
    session.close()
    print(f"Saved {len(headlines)} headlines from {site}")

def main():
    bbc_headlines = scrape_bbc()
    save_headlines("BBC", bbc_headlines)

    reuters_headlines = scrape_reuters()
    save_headlines("Reuters", reuters_headlines)

    # Display all headlines
    session = Session()
    print("\nAll headlines in DB:")
    for h in session.query(Headline).all():
        print(f"{h.site}: {h.title}")
    session.close()

if __name__ == "__main__":
    main()
