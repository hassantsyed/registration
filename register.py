import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import datetime
import time

#Opening broswer and getting site
driver = webdriver.Firefox()
driver.get('https://cas.lafayette.edu/cas/login?service=https%3A%2F%2Fbeis.lafayette.edu%2Fssomanager%2Fc%2FSSB')

#logging in
username = driver.find_element_by_id('username')
username.send_keys('username goes here')
password = driver.find_element_by_id('password')
password.send_keys('password goes here', Keys.RETURN)
#log in by pressing button
#driver.find_element_by_name('submit').click()

#navigate to registration page
driver.find_element_by_link_text('Student & Financial Aid').click()
driver.find_element_by_link_text('Registration').click()
driver.find_element_by_link_text('Add/Drop Classes').click()
#driver.find_element_by_name('submit').click()
#driver.find_element_by_xpath("//form[input/@type='submit]").click()
driver.find_element_by_xpath("//input[@value='Submit'][@type='submit']")
driver.find_element_by_xpath("//form[@action='/pls/bprod/bwskfreg.P_AltPin']/input[1]").click()

pin = driver.find_element_by_xpath("//input[@name='pin'][@type='password']")
pin = driver.find_element_by_xpath("//form[@action='/pls/bprod/bwskfreg.P_CheckAltPin']/input[1]")
pin = driver.find_element_by_xpath("//input[@name='pin']")


 
#time.sleep(1)
#print(timestamp)
# Or check if a time is between two other times
start = datetime.time(23, 00)
print(start)
end = datetime.time(23, 30)
print(end)
while(True):
	
	time.sleep(1)
	timestamp = datetime.datetime.now().time()
	print (timestamp)
	if(start <= timestamp <= end):
	
		pin.send_keys('524151', Keys.RETURN)

		crn1 = driver.find_element_by_id('crn_id1')
		crn1.send_keys('1111')
		crn2 = driver.find_element_by_id('crn_id2')
		crn2.send_keys('1111')
		crn3 = driver.find_element_by_id('crn_id3')
		crn3.send_keys('1111')
		crn4 = driver.find_element_by_id('crn_id4')
		crn4.send_keys('1111')
		crn5 = driver.find_element_by_id('crn_id5')
		crn5.send_keys('1111', Keys.RETURN)


