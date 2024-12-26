from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file = 0
query = "Realme"
for i in range(1, 2):
    driver.get(f"https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3D{query}&otracker=nmenu_sub_Electronics_0_{query}&page={i}")
    elems = driver.find_elements(By.CLASS_NAME, "Otbq5D")
    print(f"Found {len(elems)} elements")
    for elem in elems:
        file += 1
        with open(f"file{file}.html", "w", encoding="utf-8") as f:
            f.write(elem.get_attribute("outerHTML"))
    time.sleep(2)
driver.close()