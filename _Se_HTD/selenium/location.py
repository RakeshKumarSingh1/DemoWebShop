from selenium import webdriver
import time

path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver_obj = webdriver.Chrome(path)
driver_obj.get("https://demowebshop.tricentis.com/")

# time.sleep(2)
# driver_obj.maximize_window()
# time.sleep(2)
# driver_obj.minimize_window()
# time.sleep(2)
# driver_obj.maximize_window()
# time.sleep(2)
# driver_obj.refresh()
# print(driver_obj.title)
# print(driver_obj.current_url)
#driver_obj.close()
#driver_obj.quit()  #"close only current working path"

#locating the webelement using id locator

#driver_obj.find_element_by_id("small-searchterms").send_keys("books")

##########using name locator
#driver_obj.find_element_by_id("q").send_keys("books")
#driver_obj.find_element_by_class_name("button-1.search-box-button").click()
#driver_obj.find_element_by_link_text("Register").click()
#driver_obj.find_element_by_partial_link_text("Reg").click()

########USING CSS SELECTOR
#driver_obj.find_element_by_class_name("ico-login").click()
#driver_obj.find_element_by_partial_link_text("Log in").click()
#driver_obj.find_element_by_css_selector('input[value="Search store"]').click()

#########Using tag name
# links=driver_obj.find_elements_by_tag_name("a")
# print(links)
# for lin in links:
#     print(lin.text)

# links=driver_obj.find_elements_by_tag_name("div")
# print(links)
# for lin in links:
#     print(lin.text)

#########Using Xpath
#driver_obj.find_element_by_xpath("//a[text()='Register']").click()
#driver_obj.find_element_by_xpath("//a[@class='ico-register']").click()
#driver_obj.find_element_by_xpath("//a[text()='Register']").click()

#############################################################################3
#"10-11-22"

# from selenium import webdriver
# import time
# path=r"C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe"
# object1=webdriver.Chrome(path)
# object1.get("https://www.goibibo.com/")
#
# time.sleep(2)
# object1.maximize_window()