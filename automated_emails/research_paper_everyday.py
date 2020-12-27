import smtplib
import datetime as dt
import random
import csv
import pandas as pd


email = "dsc.rait@gmail.com"
password = "RAITCodeKarega"
to_addrs = "vaishdw2207@gmail.com"

now = dt.datetime.now()
print(now)
time = dt.time(hour=20, minute=35)
print(time)
weekday = now.weekday()

if weekday > -1:
    # with open('papers_ai.txt', 'r') as file:
    #     all_papers = file.read()
    #     papers = ast.literal_eval(all_papers)
    #     paper = random.choice(papers)
    #     paper_name = paper["name"]
    #     link = paper["link"]
    # print(paper_name)
    # print(link)
    with open('papers_ai.csv', 'r') as f:
        data = csv.reader(f)
        papers = list(data)
        paper = random.choice(papers)
        paper_title = paper[0]
        paper_link = paper[1]
        repo_link = paper[4]
    print(paper_title)
    print(paper_link)
    print(repo_link)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=to_addrs,
                            msg=f"Subject:Research Paper of the Day\n\nName of the Paper: {paper_title}\nLink to the Paper: {paper_link}\nLink to the github repo: {repo_link}")
        
        
    