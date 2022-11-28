import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get("file:///C:/Users/admin/OneDrive/Desktop/Selenium/demo%20(1).html")
driver.maximize_window()
time.sleep(2)
ele=driver.find_element_by_id("standard_cars")
sel_obj=Select(ele)
time.sleep(2)
sel_obj.select_by_visible_text("Audi")
time.sleep(2)
sel_obj.select_by_value("bmw")
time.sleep(2)
sel_obj.select_by_index("4")

#####Getting all the option in select car box
'''all_options = sel_obj.options
print(all_options)
for option in all_options:
    sel_obj.select_by_visible_text(option.text)
    time.sleep(2)

for index,value in enumerate(all_options):
    sel_obj.select_by_index(index)
    time.sleep(2)
'''

ele= driver.find_element_by_id("multiple_cars")
obj_ms=Select(ele)
obj_ms.select_by_visible_text("Audi")
obj_ms.select_by_visible_text("Ford")
obj_ms.select_by_value("bmw")
obj_ms.select_by_index(5)
obj_ms.all_selected_options
time.sleep(2)
obj_ms.deselect_all()
print(obj_ms.is_multiple)
print(sel_obj.is_multiple)




