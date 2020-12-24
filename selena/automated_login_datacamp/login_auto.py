from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#setting up selenium webdriver
chrome_driver_path = "/Users/dwvicy/DevTools/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#getting the page we want to automate login, in this case datacamp login
driver.get("https://www.datacamp.com/")

#getting the email input
email = driver.find_element_by_name("user[email]")

#type in values in the email input
email.send_keys("nottheemailIused@lol.com")

#getting the password input
password = driver.find_element_by_name("user[password]")

#type in values in the password input
password.send_keys("IChangedMyPasswordBeforeCommittingIdiots")


password.send_keys(Keys.ENTER)


#P.S. it will ask for human verification xD


