import requests
import time
import json
import bs4
from bs4 import BeautifulSoup
import pandas as pd
#from time import sleep

item = ''
def get_categoires(url):
    global  item
    cat_list=[]
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    try:
        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code == 200:
            html = r.text
            soup = bs4.BeautifulSoup(html, 'lxml')
            items = soup.select("#mw-normal-catlinks")
            examples = items[0]
            for items in examples.select('a'):
                if items.text == 'Categories':
                    pass
                else:
                    cat_list.append(items.text)
    except Exception as ex:
        print(str(ex))
    finally:
        return cat_list

def get_heading(url):
    global  item
    #cat_list1=[]
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    try:
       r = requests.get(url, headers=headers, timeout=10)

        if r.status_code == 200:
            html = r.text
            soup = bs4.BeautifulSoup(html, 'lxml')
            items = soup.select("#firstHeading")
            item = items[0]
            #cat_list1.append(examples.text)
    except Exception as ex:
        print(str(ex))
    finally:
        return item.text

WP_links = None
#cars_info = []
df = pd.read_excel(r'/Users/smani/Downloads/skills_taxonomy.xlsx')
skills = df["skill"].tolist()
skill_l = []
for x in skills:
    if isinstance(x,str):
        for y in x :
            if y.isalpha():
                skill_l.append(x.lower())
                break
    else:
        pass
final_skill = list(dict.fromkeys(skill_l))
#final_skill = final_skill[:30]
base_url = 'https://en.wikipedia.org/wiki/'
nowtime = time.time()
f=open("WP_Cat_" + str(nowtime) + ".json", "w+")
for i,s in enumerate(final_skill):
    url1 = '{}{}'.format(base_url, s)
    #testc = requests.get(url1)
    WP_categories = get_categoires(url1)
    WP_heading = get_heading(url1)
    if len(WP_categories)!=0 :
        cat_dict = {"Skills " : s,"WP_Heading ":WP_heading, "Categories ": WP_categories}
        #print(cat_dict)
    else :
        cat_dict = {"Skills ": s, "WP_Heading ": "Wikipage Not Found"}
    print(i)
    f.write(str(cat_dict) + ",")
f.close()
