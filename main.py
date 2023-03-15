from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
remoteDriver = webdriver.Chrome('./misc/chrome/chromedriver', chrome_options=chrome_options)
localDriver = webdriver.Chrome('./misc/chrome/chromedriver')

nexon_id_dict = [
    {'id': 'input_id', 'pw': 'input_pw'}
]

google_id_dict = [
    {'id': 'input_id'},
    {'id': 'input_id'}
]

coupon_names = ["부상없이후회없이U20아시안컵"]


def register_coupon(coupon_name, driver):
    driver.find_element(By.ID, 'strCoupon').clear()
    driver.find_element(By.ID, 'strCoupon').send_keys(coupon_name)
    sleep(1)
    driver.find_element(By.ID, 'btnReg').click()
    sleep(1)
    driver.find_element(By.ID, 'btnCommonCfm').click()
    sleep(1)


def login_nexon(e_nexon, driver):
    driver.find_element(By.ID, 'txtNexonID').send_keys(e_nexon['id'])
    driver.find_element(By.ID, 'txtPWD').send_keys(e_nexon['pw'])
    driver.find_element(By.CSS_SELECTOR, 'div.btLogin button.button01').click()
    sleep(2)


def login_naver(driver):
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'button.btNaver').click()
    sleep(2)


def login_google(e_google, driver):
    driver.find_element(By.CSS_SELECTOR, 'button.btGoogle').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div[data-identifier='%s']" % (e_google['id'])).click()
    sleep(2)


def logout(driver):
    driver.find_element(By.CSS_SELECTOR, 'button.btn_logout').click()


if __name__ == '__main__':
    remoteDriver.implicitly_wait(3)
    remoteDriver.get('https://fifamobile.nexon.com/Coupon/Index')

    localDriver.implicitly_wait(3)
    localDriver.get('https://fifamobile.nexon.com/Coupon/Index')

    # Nexon 계정
    for e_nexon in nexon_id_dict:
        login_nexon(e_nexon, localDriver)
        for coupon_name in coupon_names:
            register_coupon(coupon_name, localDriver)
        logout(localDriver)

    ## Naver 계정
    login_naver(remoteDriver)
    for coupon_name in coupon_names:
        register_coupon(coupon_name, remoteDriver)
    logout(remoteDriver)

    ## Google 계정
    for e_google in google_id_dict:
        login_google(e_google, remoteDriver)
        for coupon_name in coupon_names:
            register_coupon(coupon_name, remoteDriver)
        logout(remoteDriver)

    sleep(5)
