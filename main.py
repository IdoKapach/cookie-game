from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from threading import Timer

def update():
    for i in range(len(buttons)):
        buttons[i] = driver.find_element(By.ID, ids[i])

def buy():
    money = driver.find_element(By.ID, "money")
    prices_txt = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    prices = [product.text.split(" ")[len(product.text.split(" ")) - 1] for product in prices_txt]
    prices = [int(prices[i].replace(',', '')) for i in range(len(prices) - 2, -1, -1)]

    for i in range(len(prices)):
      if prices[i]<int(money.text):
          buttons[i].click()
          break


def truth():
    update()
    buy()
    t = Timer(7, truth)
    t.start()

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrom_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

buy_options = driver.find_elements(By.CSS_SELECTOR, "#store div")
buy_options = [buy_options[i] for i in range(len(buy_options) - 2, -1, -1)]

cookie = driver.find_element(By.ID, "cookie")

buttons = buy_options
ids = [button.get_attribute("id") for button in buttons]

t = Timer(7, truth)

t.start() # truth will be called after a 15 second interval
while True:
    time.sleep(0.001)
    cookie.click()

