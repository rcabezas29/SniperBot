from requests_html import HTMLSession
from time import sleep
from selenium import webdriver


def to_buy(url):
    driver = webdriver.Opera()
    driver.get(url)
    driver.find_element_by_class_name("")


def check_price(url):
    session = HTMLSession()
    a = session.get(url)
    price = float(str(a.html.find("#precio-main")[0]).split(" ")[6].partition("=")[2].replace("'", ""))
    print(price)
    return price


# Check if your article has stock or not (it changes for every website)
def check_stock(url):
    session = HTMLSession()
    a = session.get(url)
    buy_zone = a.html.find("#articleToBasket")
    if len(buy_zone) > 0:
        return True
    else:
        return False


def main():
    url = "https://www.pccomponentes.com/asus-geforce-gt-1030-2gb-gddr5"
    while True:
        stock = check_stock(url)
        price = check_price(url)
        if stock == True and price < 400:
            to_buy(url)
        sleep(5000)


if __name__ == "__main__":
    main()
