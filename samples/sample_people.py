from linkedin_scraper import Person, actions
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

email = "";
password = "";


people = ["jonmacaskill", "andrew-huberman"]

for p in people:
    driver = webdriver.Chrome(options=options)
    actions.login(driver, email, password)
    url = "https://www.linkedin.com/in/"+p
    person = Person(linkedin_url=url, driver=driver)
    print(person)
