from selenium import webdriver
import pickle
import pprint

#setting up selenium webdriver
chrome_driver_path = "/Users/dwvicy/DevTools/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#getting the mlh page
driver.get("https://mlh.io/seasons/2021/events")


events = {}
#getting the data from the website
event_names = driver.find_elements_by_class_name("event-name")
print(type(event_names))
event_dates = driver.find_elements_by_class_name("event-date")
event_links = driver.find_elements_by_css_selector(".event-wrapper a")


#looping through the data to print it in the form of a dict
for i in range(len(event_names)):
    events[i] = {
        "name": event_names[i].text,
        "date" : event_dates[i].text,
        "link": event_links[i].get_attribute("href"),    
    }

print(events)

#formatting the dict and converting to string
event_dict = pprint.pformat(events)
    
#writing the dict into a file called mlh.txt   
try:
    event_txt = open('events_mlh.txt', 'wt')
    event_txt.write(event_dict)
    event_txt.close()
except: 
    print("Unable to open file")
    
    