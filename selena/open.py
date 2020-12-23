from selenium import webdriver

#setting up selenium webdriver
chrome_driver_path = "/Users/dwvicy/DevTools/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#open a webpage

driver.get("https://www.myntra.com/jewellery-set/priyaasi/priyaasi-oxidised-silver-plated-german-silver-jewellery-set/12361312/buy")
price = driver.find_element_by_tag_name("strong")
print(price.text)

# driver.close()
driver.quit()