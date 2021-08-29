import requests, bs4
from notifypy import Notify

site = "https://www.uk.emb-japan.go.jp/itpr_en/index_000072.html"
res = requests.get(site)

notification = Notify()
notification.title = "Japan Working Holiday Visa"

try:
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    whv = soup.select("#main > div:nth-child(4) > div > div > div > p > font > strong")[0].text.strip()
    lastUpdated = soup.select("#main > div:nth-child(2)")[0].text.strip()
except:
    notification.message = f"Error \n {site}"    
    notification.send()

if whv == "Due to restrictions relating to the coronavirus pandemic, we are not able to take applications for the Working Holiday Visa.":
    if lastUpdated == "2021/7/1":
        pass
        #will eventually hash out the below statements once I'm sure that the script is running automatically using cron
        #notification.message = f"No Update \n{site}"
        #notification.send()
    else:
        notification.message = f"Date Updated - Working Holiday Visas still not available \n{site}"
        notification.send()
else:
    notification.message = f"See website for update \n{site}"
    notification.send()