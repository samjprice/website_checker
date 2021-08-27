import requests, bs4
from notifypy import Notify

res = requests.get("https://www.uk.emb-japan.go.jp/itpr_en/index_000072.html")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
whv = soup.select("#main > div:nth-child(4) > div > div > div > p > font > strong")[0].text.strip()
lastUpdated = soup.select("#main > div:nth-child(2)")[0].text.strip()

notification = Notify()
notification.title = "Japan Working Holiday Visa"

if (whv == "Due to restrictions relating to the coronavirus pandemic, we are not able to take applications for the Working Holiday Visa."):
    if lastUpdated == "2021/7/1":
        pass
        #will eventually hash out the below statements once I'm sure that the script is running automatically using cron
        notification.message = "No Update \nhttps://www.uk.emb-japan.go.jp/itpr_en/index_000072.html"
        notification.send()
    else:
        notification.message = "Date Updated - Working Holiday Visas still not available \nhttps://www.uk.emb-japan.go.jp/itpr_en/index_000072.html"
        notification.send()
else:
    notification.message = "See website for update \nhttps://www.uk.emb-japan.go.jp/itpr_en/index_000072.html"
    notification.send()