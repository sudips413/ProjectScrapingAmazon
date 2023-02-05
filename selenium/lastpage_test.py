from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# set up selenium webdriver
driver = webdriver.Edge(executable_path=r"D:\coderush\scrap\selenium\amazonscrap\msedgedriver.exe")
driver.get("https://www.amazon.com/s?k=headphones&rh=n%3A172282%2Cp_89%3AJBL&dc&ds=v1%3A5eHFd79a6%2BwFz6Y26I2lZxb7D%2BE5kOT71zyRSWfkLOU&qid=1675491483&rnid=2528832011&ref=sr_nr_p_89_1")
time.sleep(5)

#find the last page
response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding="utf-8", request=None)
try:
    spans = response.css('div.s-pagination-container>span.s-pagination-strip>span.s-pagination-item::text').getall()
    
    print(spans[-1])    
except:
    print("No last page")




# close the webdriver
driver.close()
# basic selenium to open browser, search samsung and extract device name