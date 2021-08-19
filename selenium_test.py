
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
url = ("https://www.odebractelefon.pl/numer-telefonu/683647964")
#url = ("https://www.odebractelefon.pl/numer-telefonu/539263674")
driver = webdriver.Chrome(options=options)
driver.get(url)
# op = driver.find_element_by_class_name('active')
try:
    op = driver.find_element_by_xpath("//html/body/div/div/div/div[1]/article/div[1]/div[2]/div[1]/ul/li[1]")
    print(op.text)
except NoSuchElementException:
    print("Brak")
driver.quit()
