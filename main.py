from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from optparse import OptionParser

nexon_id_dict = [
    {'id': 'input_id', 'pw': 'input_pw'}
]

google_id_dict = [
    {'id': 'input_id'},
    {'id': 'input_id'}
]


def click_element(element, delay=1):
    element.click()
    sleep(delay)


def register_coupon(coupon_names, driver):
    manager_name = driver.find_element(By.CSS_SELECTOR, "div#coupon div.user p").text
    for coupon_name in coupon_names:
        driver.find_element(By.ID, 'strCoupon').clear()
        driver.find_element(By.ID, 'strCoupon').send_keys(coupon_name)
        sleep(1)
        click_element(driver.find_element(By.ID, 'btnReg'))
        click_element(driver.find_element(By.CSS_SELECTOR, "div.complete div.button button.btn_type_blue"))
        print(f"쿠폰등록완료 {manager_name} 쿠폰명:{coupon_name}")


def register_coupon_auto(driver):
    driver.find_element(By.ID, 'strCoupon').clear()
    sleep(1)
    manager_name = driver.find_element(By.CSS_SELECTOR, "div#coupon div.user p").text
    avail_coupons = driver.find_elements(By.CSS_SELECTOR, "div#coupon li.active button")

    if len(avail_coupons) == 0:
        print(f"사용가능한 쿠폰이 없습니다.({manager_name})")
        return

    while len(avail_coupons) > 0:
        click_element(avail_coupons[0])
        click_element(driver.find_element(By.ID, 'cbtn_cfm'))
        coupon_name = driver.find_element(By.CSS_SELECTOR, "#strCoupon").get_attribute('value')
        click_element(driver.find_element(By.ID, 'btnReg'))
        click_element(driver.find_element(By.CSS_SELECTOR, "div.complete div.button"))
        print(f"쿠폰등록완료 {manager_name} 쿠폰명:{coupon_name}")
        avail_coupons = driver.find_elements(By.CSS_SELECTOR, "div#coupon li.active button")


def login_nexon(e_nexon, driver):
    driver.find_element(By.ID, 'txtNexonID').clear()
    driver.find_element(By.ID, 'txtNexonID').send_keys(e_nexon['id'])
    driver.find_element(By.ID, 'txtPWD').clear()
    driver.find_element(By.ID, 'txtPWD').send_keys(e_nexon['pw'])
    click_element(driver.find_element(By.CSS_SELECTOR, 'div.btLogin button.button01'), delay=3)


def login_facebook(driver):
    click_element(driver.find_element(By.CSS_SELECTOR, 'button.btFacebook'), delay=3)


def login_naver(driver):
    click_element(driver.find_element(By.CSS_SELECTOR, 'button.btNaver'), delay=3)


def login_google(e_google, driver):
    click_element(driver.find_element(By.CSS_SELECTOR, 'button.btGoogle'))
    click_element(driver.find_element(By.CSS_SELECTOR, "div[data-identifier='%s']" % (e_google['id'])), delay=3)


def logout(driver):
    click_element(driver.find_element(By.CSS_SELECTOR, 'button.btn_logout'), delay=3)


def load_chromedriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    remote_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    remote_driver.implicitly_wait(3)
    remote_driver.get('https://fifamobile.nexon.com/Coupon/Index')

    return remote_driver


def register_nexon_account(nexon_id_dicts, driver, coupon_name, automatic):
    for e_nexon in nexon_id_dicts:
        login_nexon(e_nexon, driver)
        if coupon_name is not None:
            register_coupon(coupon_name, driver)
        if automatic:
            register_coupon_auto(driver)
        logout(driver)


def register_naver_account(driver, coupon_name, automatic):
    login_naver(driver)
    if coupon_name is not None:
        register_coupon(coupon_name, driver)
    if automatic:
        register_coupon_auto(driver)
    logout(driver)


def register_google_account(google_id_dicts, driver, coupon_name, automatic):
    for e_google in google_id_dicts:
        login_google(e_google, driver)
        if coupon_name is not None:
            register_coupon(coupon_name, driver)
        if automatic:
            register_coupon_auto(driver)
        logout(driver)


def register_facebook_account(driver, coupon_name, automatic):
    login_facebook(driver)
    if coupon_name is not None:
        register_coupon(coupon_name, driver)
    if automatic:
        register_coupon_auto(driver)
    logout(driver)


def main():
    parser = OptionParser()
    parser.add_option("-a", "--auto", action="store_true", dest="automatic", default=False,
                      help="is automatic registration")
    parser.add_option("-c", "--coupon", action="append", metavar="COUPON_NAME", dest="coupon_name")
    (options, args) = parser.parse_args()

    remote_driver = load_chromedriver()

    register_nexon_account(nexon_id_dict, remote_driver, options.coupon_name, options.automatic)

    register_naver_account(remote_driver, options.coupon_name, options.automatic)

    register_google_account(google_id_dict, remote_driver, options.coupon_name, options.automatic)

    register_facebook_account(remote_driver, options.coupon_name, options.automatic)


if __name__ == '__main__':
    main()
    sleep(5)
