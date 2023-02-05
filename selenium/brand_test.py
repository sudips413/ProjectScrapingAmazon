from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# set up selenium webdriver
driver = webdriver.Edge(executable_path=r"D:\coderush\scrap\selenium\amazonscrap\msedgedriver.exe")
driver.get("https://www.amazon.com/")
time.sleep(5) 
# perform a search on Amazon using Selenium
search_field = driver.find_element(By.ID, "twotabsearchtextbox")

search_field.send_keys("headphone")

search_field.send_keys(Keys.RETURN)
response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding="utf-8")

brandname= response.css("div#brandsRefinements>ul.a-spacing-medium>li> span > a > span::text").getall()
for brand_name in brandname:
    click_brand = driver.find_element(By.LINK_TEXT, brand_name)
    click_brand.click()
    time.sleep(3)
    response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding="utf-8")
    try:
        spans = response.css('div.s-pagination-container>span.s-pagination-strip>span.s-pagination-item::text').getall()
        
        page=spans[-1]  
    except:
        page =0
    if page !=0:
        for i in range(1,int(page)+1):
            print(brand_name,i)
            device_names = response.css('span.a-text-normal::text').getall()
            time.sleep(2)
            for device_name in device_names:
                #click on device_name link                
                if device_name == "RESULTS" or device_name == " " or device_name == "MORE RESULTS":
                    pass
                else:
                    device_element = driver.find_element(By.LINK_TEXT, device_name)
                    device_element.click()                    
                    driver.implicitly_wait(5)
                    response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding="utf-8", request=None)
                    Brand = response.css('.po-brand>td>span.po-break-word::text').get()
                    Model = response.css('.po-model_name>td>span.po-break-word::text').get()
                    Ratings = response.css('span#acrCustomerReviewText::text').get()
                    price = (response.css('span.a-offscreen::text').get())[1:]
                    Color = response.css('.po-color>td>span.po-break-word::text').get()
                    weight = response.css('#productDetails_detailBullets_sections1 > tbody > tr:nth-child(2) > td::text').get()
                    yield{                    
                        "Model": Model,
                        "Brand": Brand,
                        "weight": weight,
                        "Ratings": Ratings,
                        "Price": price,
                        "Color": Color,
                    }
                    go back to the search results page
                    driver.implicitly_wait(5)
                    driver.back()
            time.sleep(5)
            next_button = WebDriverWait(driver,200).until(EC.element_to_be_clickable((By.CLASS_NAME,"s-pagination-next")))                
            next_button.click()
            driver.implicitly_wait(5) 
        driver.get("https://www.amazon.com/s?k=headphone") 
    else:
        driver.get("https://www.amazon.com/s?k=headphone")

driver.close()
# basic selenium to open browser, search samsung and extract device name