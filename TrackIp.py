# Made important imports.
from bs4 import BeautifulSoup
import requests
information = {}

# This function runs at the beginning of the IP class.
def searchIp(x):
    global information
    url = "https://whatismyipaddress.com/ip/" + x
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    data = soup.find("div", id="main_content_3rd")
    tables = data.find_all('table')[1]
    ths = tables.find_all("th")
    tds = tables.find_all("td")
    j = str(ths)
    p = str(tds)
    titles = []
    info = []
    for item in j.split("</th>"):
        if "<th>" in item:
            titles.append(item[item.find("<th>")+len("<th>"):])
    for item in p.split("</td>"):
        if "<td>" in item:
            info.append(item[item.find("<td>")+len("<td>"):])
    for i in range(0, len(info)):
        information[str(titles[i])] = str(info[i])
    return information
        
# Needed class.
class ip:
    def __init__(self, address):
        global information
        searchIp(address)
        self.address = address
        self.info = information

    def zipcode(self):
        return self.info["Postal Code:"]

    def latitude(self):
        return self.info["Latitude:"]

    def longitude(self):
        return self.info["Longitude:"]

    def continent(self):
        return self.info["Continent:"]

    def city(self):
        return self.info["City:"]

    def country(self):
        return self.info["Country:"]

    def state(self):
        return self.info["State/Region:"]
