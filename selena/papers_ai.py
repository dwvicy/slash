from selenium import webdriver
import pickle
import pprint

#setting up selenium webdriver
chrome_driver_path = "/Users/dwvicy/DevTools/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#getting the papers with code page
driver.get("https://paperswithcode.com/greatest")


papers = {}

#getting the data from the website
paper_names = driver.find_elements_by_css_selector(".item h1 a")
print(type(paper_names))

#looping through the data to get it in the form of a dict
for name in paper_names:
    print(name.get_attribute("href"))

for i in range(len(paper_names)):
    papers[i] = {
        "name": paper_names[i].text,
        "link": paper_names[i].get_attribute("href"),    
    }

#formatting dict and converting it into str to write it into the file paper_ai.txt
paper_dict = pprint.pformat(papers)
    
#writing the dict into paper_ai.txt  
try:
    paper_txt = open('papers_ai.txt', 'wt')
    paper_txt.write(paper_dict)
    paper_txt.close()
except: 
    print("Unable to open file")
    
    