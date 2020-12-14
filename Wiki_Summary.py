import pandas as pd
import wikipedia
import time

nowtime = time.time()

f1=open("LastDesc_WP" + str(nowtime) + ".json", "w+")
f2=open("LastRest_WP" + str(nowtime) + ".json", "w+")

df = pd.read_csv(r'/Users/smani/Downloads/newskills.csv')
slist = df["display_name"].tolist()
sdict = {}
relist = []

for i in slist[:308] :
    try :
        sdict["Skill"]= i
        sdict["Description"]= wikipedia.summary(i,sentences=2)
        f1.write((str(sdict) + ","))
        #print(sdict)

    except wikipedia.exceptions.DisambiguationError as e :
        relist.append(i)
        f2.write((str(relist) + ","))

    except wikipedia.exceptions.PageError as e :
        relist.append(i)
        f2.write((str(relist) + ","))

    except ConnectionError as e:
        pass
