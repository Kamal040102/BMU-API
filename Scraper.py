from bs4 import BeautifulSoup
import requests
import json

def scrapCircular():
    page = requests.get("https://www.bmusurat.ac.in/Circular").text
    soup = BeautifulSoup(page, "lxml")
    mainDict = {}
    i = 0
    panel = soup.find("div", class_="ui-tabs-panel")
    trows = panel.find_all("tr", class_="odd")
    for trow in trows:
        date = trow.find("td", class_="circular").text
        moreDetail = trow.find("td", class_="cellfeat")
        title = moreDetail.find("a").text
        link = moreDetail.find("a")['href']
        # print(date, title, link)
        mainDict[i] = {"date":date,"title":title,"link":link}
        i += 1
    mainDict = json.dumps(mainDict)
    return mainDict