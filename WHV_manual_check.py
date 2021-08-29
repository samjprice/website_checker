#This is my manual run checker which always sends notifications

import bs4
import requests

from notifypy import Notify


APP_NAME = "WHV Notifier"
SITE_URL = "https://www.uk.emb-japan.go.jp/itpr_en/index_000072.html"

res = requests.get(SITE_URL)

try:
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    whv = soup.select("#main > div:nth-child(4) > div > div > div > p > font > strong")[0].text.strip()
    last_updated = soup.select("#main > div:nth-child(2)")[0].text.strip()
except:
    message = f"Error \n {SITE_URL}"    

if whv == "Due to restrictions relating to the coronavirus pandemic, we are not able to take applications for the Working Holiday Visa.":
    if last_updated == "2021/7/1":
        message = f"No Update \n{SITE_URL}"
    else:
        message = f"Date Updated - Working Holiday Visas still not available \n{SITE_URL}"
else:
    message = f"See website for update \n{SITE_URL}"

notification = Notify("Japan Working Holiday Visa", message, APP_NAME)
notification.send()