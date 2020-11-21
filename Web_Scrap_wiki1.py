import  pandas as df
import pandas as pd
import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup
import time
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
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
final_skill = final_skill[3398:]
base_url  = 'https://en.wikipedia.org/wiki/'
nowtime = time.time()
f=open("WP_scrapnew_" + str(nowtime) + ".json", "w+")
final_data = []

for i,s in enumerate(final_skill):
    skill_list=[]
    url1 = '{}{}'.format(base_url, s)
    url2 = '{}{}{}'.format(base_url,s,"_(disambiguation)")

    #proxy_host = "proxy.crawlera.com"
    #proxy_port = "8010"
    #proxy_auth = "<CRAWLERA API KEY>:" # Make sure to include ':' at the end
    #proxies = {"https": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
      #"http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}

    resp1 = requests.get(url1,timeout = None, headers=headers)
    resp2 = requests.get(url2,timeout = None, headers=headers)
    soup1 = BeautifulSoup(resp1.text, 'html.parser')
    soup2 = BeautifulSoup(resp2.text, 'html.parser')
    if resp1.status_code == 200:
        for item1 in soup1.select("#firstHeading"):
            skill_dict = {'Skill':s, 'URL':url1, 'PageHeading':item1.text}
    else :
        skill_dict={'Skill':s, 'URL':"Web page does not exist", 'PageHeading': "NA"}
    if resp2.status_code == 200:
        for item2 in soup2.select(".mw-headline"):
            skill_list.append(item2.text)
            #print(skill_list)
        skill_dict['Other_use']= skill_list
    else :
        skill_dict['Other_use']= "NA"
    print(i)
    f.write(str(skill_dict)+",")
        #final_data.append(skill_dict)
f.close()
