from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver1=webdriver.Chrome(path)
driver1.get('https://www.facebook.com/r.php')
time.sleep(2)
driver1.maximize_window()
driver1.find_element_by_name('firstname').send_keys('Rakesh')
time.sleep(2)
driver1.find_element_by_name('lastname').send_keys('Singh')
time.sleep(2)
driver1.find_element_by_name('reg_email__').send_keys('rks@gmail.com')
time.sleep(2)
driver1.find_element_by_name('reg_email_confirmation__').send_keys('rks@gmail.com')
time.sleep(2)
driver1.find_element_by_name('reg_passwd__').send_keys('rks@123')
time.sleep(2)

day = driver1.find_element_by_name('birthday_day')
day_obj = Select(day)
day_obj.select_by_visible_text('10')
time.sleep(2)

mon=driver1.find_element_by_name('birthday_month')
mon_obj=Select(mon)
mon_obj.select_by_visible_text('Dec')
time.sleep(2)

year=driver1.find_element_by_name('birthday_year')
year_obj=Select(year)
year_obj.select_by_visible_text('1999')

driver1.find_element_by_xpath("//label[text()='Male']/..//input[@value='2']").click()
time.sleep(2)
driver1.find_element_by_name('websubmit').click()
# driver1.find_element_by_name('birthday_day').send_keys('08')
# time.sleep(2)
# driver1.find_element_by_name('birthday_month').send_keys('Dec')
# time.sleep(2)
# driver1.find_element_by_name('birthday_year').send_keys('1999')
# time.sleep(2)
#driver1.find_element_by_class_name('')
