from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from pyautogui import press
from time import sleep
from selenium import webdriver as webdriver
import json
import random
import time
print(""" ____                 __ _           ____        _   
|  _ \               / _| |         |  _ \      | |  
| |_) | _____      _| |_| | _____  _| |_) | ___ | |_ 
|  _ < / _ \ \ /\ / /  _| |/ _ \ \/ /  _ < / _ \| __|
| |_) | (_) \ V  V /| | | |  __/>  <| |_) | (_) | |_ 
|____/ \___/ \_/\_/ |_| |_|\___/_/\_\____/ \___/ \__|
                                                     
                                                     
""")
config = json.loads(open('config.json').read())
link = input("Paste product link here: ")
headlessBool = input("Would you like to run headless?")
options = Options()
if headlessBool == "y":
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    #options.add_argument("--disable-extensions")
    #options.add_argument("--disable-gpu")
else:
    options.headless = False
    options.add_argument("--disable-gpu")
defDriver = webdriver.Chrome(config[0], options=options)
shipping = json.loads(open('shipping.json').read())
billing = json.loads(open('billing.json').read())

def sendForm(runs):
        defDriver.get(link)
        sleep(0.5)
        next1 = defDriver.find_element_by_id("add-to-cart")
        next1.click()
        sleep(0.2)
        defDriver.get("https://www.bowflex.com/cart")
        sleep(0.2)
        next2 = defDriver.find_element_by_xpath("""//*[@id="checkout-form"]/fieldset/button""")
        next2.click()
        print("added product to cart")
        sleep(0.2)
        email1 = defDriver.find_element_by_xpath("""//*[@id="dwfrm_singleshipping_shippingAddress_email_emailAddress"]""")
        email1.send_keys(shipping[0])
        name1 = defDriver.find_element_by_xpath("""//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_firstName"]""")
        name1.send_keys(shipping[1])
        name2 = defDriver.find_element_by_xpath("""//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_lastName"]""")
        name2.send_keys(shipping[2])
        addy1 = defDriver.find_element_by_xpath("""//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_address1"]""")
        addy1.send_keys(shipping[3])
        city1 = defDriver.find_element_by_xpath("""//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_city"]""")
        city1.send_keys(shipping[4])
        state1 = defDriver.find_element_by_xpath("""//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_states_state"]""")
        state1.send_keys(shipping[5])
        zip1 = defDriver.find_element_by_xpath("""//*[@id="dwfrm_singleshipping_shippingAddress_addressFields_postal"]""")
        zip1.send_keys(shipping[6])
        sleep(0.2)
        contToPayment1 = defDriver.find_element_by_xpath("""//*[@id="shippingSubmitButton"]""")
        contToPayment1.click()
        print("submitting billing")
        cardType = defDriver.find_element_by_xpath("""//*[@id="dwfrm_billing_paymentMethods_creditCard_type"]""")
        cardType.send_keys(billing[0])
        cardNum = defDriver.find_element_by_xpath("""//*[@id="dwfrm_billing_paymentMethods_creditCard_number"]""")
        cardNum.send_keys(billing[1])
        nameOnCard = defDriver.find_element_by_xpath("""//*[@id="dwfrm_billing_paymentMethods_creditCard_owner"]""")
        nameOnCard.send_keys(billing[2])
        expMonth = defDriver.find_element_by_xpath("""//*[@id="dwfrm_billing_paymentMethods_creditCard_month"]""")
        expMonth.send_keys(billing[3])
        expYear = defDriver.find_element_by_xpath("""//*[@id="dwfrm_billing_paymentMethods_creditCard_year"]""")
        expYear.send_keys(billing[4])
        secCode = defDriver.find_element_by_xpath("""//*[@id="dwfrm_billing_paymentMethods_creditCard_cvn"]""")
        secCode.send_keys(billing[5])
        phoneNum = defDriver.find_element_by_xpath("""//*[@id="dwfrm_billing_paymentMethods_creditCard_phone"]""")
        phoneNum.send_keys(billing[6])
        sleep(0.2)
        continueToPlace = defDriver.find_element_by_xpath("""//*[@id="billingSubmitButton"]""")
        continueToPlace.click()
        sleep(0.2)
        print("placing order")
        placeOrderButton = defDriver.find_element_by_xpath("""//*[@id="summaryPageForm"]/div[2]/button""")
        placeOrderButton.click()
        print("""check email""")
        sleep(60)
        
        

def main():
    runsMade = 0
    for _ in range(1, 100):
        try:
            sendForm(runsMade)
            runsMade += 1
        except Exception as e:
            print("Item out of stock. Retrying")

            
main()
