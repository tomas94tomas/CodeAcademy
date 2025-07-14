from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

EDGEDRIVER_PATH = r"E:\DevOps\Project\32-DB-Webscrape\msedgedriver.exe"

edge_options = Options()
# Optional: Run headless
# edge_options.add_argument('--headless')

service = Service(EDGEDRIVER_PATH)
driver = webdriver.Edge(service=service, options=edge_options)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()