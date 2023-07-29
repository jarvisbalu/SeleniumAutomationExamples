from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver")

driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_4b3e4wrxds_b&adgrpid=60639568242&hvpone=&hvptwo=&hvadid=617721280315&hvpos=&hvnetw=g&hvrand=17136086855163045803&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061750&hvtargid=kwd-311187680635&hydadcr=5841_2362028")
driver.maximize_window()
print(driver.title)


from selenium import webdriver

driver = webdriver.Edge(executable_path="C:\\browserdrivers\msedgedriver")

driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_4b3e4wrxds_b&adgrpid=60639568242&hvpone=&hvptwo=&hvadid=617721280315&hvpos=&hvnetw=g&hvrand=17136086855163045803&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061750&hvtargid=kwd-311187680635&hydadcr=5841_2362028")
driver.maximize_window()
print(driver.title)


from selenium import webdriver


from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())


driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_4b3e4wrxds_b&adgrpid=60639568242&hvpone=&hvptwo=&hvadid=617721280315&hvpos=&hvnetw=g&hvrand=17136086855163045803&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061750&hvtargid=kwd-311187680635&hydadcr=5841_2362028")
driver.maximize_window()
print(driver.title)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID, 'login-input').send_keys('sample@gmail.com')
        time.sleep(5)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.XPATH, "(//input[@id='login-input'])[1]").send_keys('sample@gmail.com')
        time.sleep(5)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys('sample@gmail.com')
        time.sleep(5)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Yatra for Business").click()
        time.sleep(5)

findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()