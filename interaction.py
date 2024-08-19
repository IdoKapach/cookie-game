from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from threading import Timer

def update():
    global money,buy_options, prices
    money = driver.find_element(By.ID, "money")
    buy_options = driver.find_elements(By.CSS_SELECTOR, "#store div")
    prices_txt = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    prices = [product.text.split(" ")[len(product.text.split(" ")) - 1] for product in prices_txt]

    buy_options = [buy_options[i] for i in range(len(buy_options) - 2, -1, -1)]
    prices = [int(prices[i].replace(',', '')) for i in range(len(prices) - 2, -1, -1)]

def buy():
    print("enter")
    for i in range(0, len(buy_options)):
        update()
        buy_options[i].click()
    t = Timer(5, buy)
    t.start()


chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrom_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

money = driver.find_element(By.ID, "money")
buy_options = driver.find_elements(By.CSS_SELECTOR, "#store div")
prices_txt = driver.find_elements(By.CSS_SELECTOR, "#store div b")
prices = [product.text.split(" ")[len(product.text.split(" ")) - 1] for product in prices_txt]

buy_options = [buy_options[i] for i in range(len(buy_options) - 2, -1, -1)]
prices = [int(prices[i].replace(',', '')) for i in range(len(prices) - 2, -1, -1)]

cookie_button = driver.find_element(By.ID, "cookie")
t = Timer(5, buy)
t.start()


while True:
    time.sleep(0.02)
    cookie_button.click()