from selenium import webdriver
import pickle
import pprint

#setting up selenium webdriver
chrome_driver_path = "/Users/dwvicy/DevTools/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#getting the mlh page
driver.get("https://paperswithcode.com/greatest")


papers = {}

paper_names = driver.find_elements_by_css_selector(".item h1 a")
print(type(paper_names))
# paper_links = driver.find_elements_by_class_name("_8w6a _8w6e _8w61")

for name in paper_names:
    print(name.get_attribute("href"))

for i in range(len(paper_names)):
    papers[i] = {
        "name": paper_names[i].text,
        "link": paper_names[i].get_attribute("href"),    
    }

paper_dict = pprint.pformat(papers)
    
    
try:
    paper_txt = open('papers_ai.txt', 'wt')
    paper_txt.write(paper_dict)
    paper_txt.close()
except: 
    print("Unable to open file")
    
    