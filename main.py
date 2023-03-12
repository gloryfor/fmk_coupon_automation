from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#

driver = webdriver.Chrome('./misc/chrome/chromedriver')
nexon_id = ""
nexon_pw = ""
coupon_names = ["U20아시안컵토너먼트시작", "a"]

def register_coupon(coupon_name):
    sleep(2)
    driver.find_element(By.ID, 'strCoupon').clear()
    driver.find_element(By.ID, 'strCoupon').send_keys(coupon_name)
    sleep(1)
    driver.find_element(By.ID, 'btnReg').click()
    sleep(1)
    driver.find_element(By.ID, 'btnCommonCfm').click()
    sleep(1)

if __name__ == '__main__':
    driver.implicitly_wait(3)
    driver.get('https://fifamobile.nexon.com/Coupon/Index')
    driver.find_element(By.ID, 'txtNexonID').send_keys(nexon_id)
    driver.find_element(By.ID, 'txtPWD').send_keys(nexon_pw)
    driver.find_element(By.CSS_SELECTOR, 'div.btLogin button.button01').click()
    for coupon_name in coupon_names:
        register_coupon(coupon_name)
    driver.find_element(By.CSS_SELECTOR, 'button.btn_logout').click()

    ## 까나리1
    # driver.find_element(By.CSS_SELECTOR, 'button.btNaver').click()

    sleep(5)

