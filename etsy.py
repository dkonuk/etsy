from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver_mail = webdriver.Chrome(options=chrome_options)

mail_url = "https://www.mail7.io/"

driver_mail.get(mail_url)
print(driver_mail.title)
x = driver_mail.find_element(By.CSS_SELECTOR, "form.inboxform:nth-child(3) > div:nth-child(1) > input:nth-child(1)")
mail = "asdas12345"
mail_address = "asdas12345@mail7.io"
x.send_keys(mail)
x.send_keys(Keys.RETURN)
time.sleep(1)
driver_mail.find_element(By.CSS_SELECTOR, "button.btn:nth-child(1)")
time.sleep(1)

url = "https://www.etsy.com/"
driver_mail.get(url)
time.sleep(5)
try:
  driver_mail.find_element(By.XPATH, '//*[@id="gdpr-single-choice-overlay"]/div/div[2]  /div[2]').click()
  time.sleep(5)
except:
  driver_mail.find_element(By.CSS_SELECTOR, '//*[@id="gnav-header-inner"]/div[4]/nav/ul/li[1]/button').click()
  
  time.sleep(2)
time.sleep(1)
driver_mail.find_element(By.XPATH, '//*[@id="join_neu_email_field"]').click()
#driver_mail.find_element(By.XPATH, '//*[@id="join_neu_email_field"]').click()
driver_mail.find_element(By.XPATH, '//*[@id="join_neu_email_field"]').send_keys("asdas12345@mail7.io")
driver_mail.find_element(By.XPATH, "//input[@id='join_neu_first_name_field']").click()
driver_mail.find_element(By.XPATH, "//input[@id='join_neu_first_name_field']").send_keys("Camilla")
driver_mail.find_element(By.XPATH, '//*[@id="join_neu_password_field"]').click()
driver_mail.find_element(By.XPATH, '//*[@id="join_neu_password_field"]').send_keys("19833131")
driver_mail.find_element(By.XPATH, '//*[@id="join-neu-form"]/div[1]/div/div[7]/div/button').click()
time.sleep(4)

#using search to find cow
driver_mail.find_element(By.CSS_SELECTOR, "#global-enhancements-search-query").send_keys("Highland Cow Gallery")
time.sleep(3)
driver_mail.find_element(By.CSS_SELECTOR, "#global-enhancements-search-query").send_keys(Keys.ENTER)

time.sleep(3)

results_locator = (By.CSS_SELECTOR, "#content > div > div.wt-bg-white.wt-grid__item-md-12.wt-pl-xs-1.wt-pr-xs-0.wt-pr-md-1.wt-pl-lg-0.wt-pr-lg-0.wt-bb-xs-1 > div > div.wt-mt-xs-3.wt-text-black > div.wt-grid.wt-pl-xs-0.wt-pr-xs-0.search-listings-group > div:nth-child(2)")
expected_result = "DartPrintables"


variable = 1  # Initialize variable before using it in the loop

while variable > 0:  # Use the correct variable name in the loop condition
    etsy_url = f"https://www.etsy.com/search?q=highland+cow+gallery+wall+set&page={variable}&ref=pagination"
    link = "www.etsy.com/listing/1310025795/highland-cow-gallery-wall-set-of-three?click_key=84e98f01dff13c0d2a1fe74a62acd71e26c02489%3A1310025795&click_sum=1f6d400b&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=highland+cow+gallery+wall+set&ref=search_grid-11031-2-8&pro=1"

    driver_mail.get(etsy_url)
    time.sleep(3)
    try:
        original_window = driver_mail.current_window_handle

        # Check we don't have other windows open already
        assert len(driver_mail.window_handles) == 1

        driver_mail.find_element(By.CSS_SELECTOR, "img[elt='Highland Cow Gallery Wall Set, Set of Three Prints, Digital Download, Nature Wall Art, Home Decor, Nursery Decor, Animal Photography']").click()
        time.sleep(2)
        print("ok1")
        #WebDriverWait.until(EC.number_of_windows_to_be(2))
        print("ok2")
        for window_handle in driver_mail.window_handles:
            if window_handle != original_window:
                driver_mail.switch_to.window(window_handle)
                break
        time.sleep(2)
        driver_mail.find_element(By.XPATH, "//div[@class='image-col wt-order-xs-1 wt-mb-lg-6']//div[1]//div[2]//button[1]//div[1]//span[1]//*[name()='svg']").click()
        time.sleep(1)
        print("favorited")
        break

    except:
        variable = variable + 1  # Increment the variable within the loop
