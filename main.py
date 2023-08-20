from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)
driver.implicitly_wait(1)
data=[]

for i in range(1,2): # 1,and 2 is page number which start from 1 to 2 replace the 2 to another page number.
    driver.get(f'https://www.amazon.in/s?k=bluetooth+headphone&i=electronics&page={i}&qid=1692552023&ref=sr_pg_2')
    items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
    for item in items:
        name = item.find_element(By.XPATH, './/span[@class="a-size-base-plus a-color-base a-text-normal"]')
        sign = item.find_elements(By.XPATH, './/span[@class="a-price-symbol"]')
        price = item.find_elements(By.XPATH, './/span[@class="a-price-whole"]')
        sponsor = item.find_elements(By.XPATH, './/span[@class="aok-inline-block puis-sponsored-label-info-icon"]')
        data_asin = item.get_attribute("data-asin")
        if len(sponsor)>0:
            sponsored= True;
        else:
            sponsored= False;
        data.append({"product_title":name.text,"price":sign[0].text+" "+price[0].text,"sponsored":sponsored,"asin":data_asin})
driver.quit()
print(data)
