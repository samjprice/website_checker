import requests, bs4, notify2

res = requests.get("https://www.uk.emb-japan.go.jp/itpr_en/index_000072.html")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
whv = soup.select("#main > div:nth-child(4) > div > div > div > p > font > strong")[0].text.strip()
lastUpdated = soup.select("#main > div:nth-child(2)")[0].text.strip()

def notif(message):
    notify2.init("Japan Working Holiday Visa")
    return notify2.Notification("Japan Working Visa", message, "python").show()

if (whv == "Due to restrictions relating to the coronavirus pandemic, we are not able to take applications for the Working Holiday Visa."):
    if lastUpdated == "2021/7/1":
        pass
        #will eventually hash out the below statements once I'm sure that the script is running automatically using cron
        notif("No Update \nhttps://www.uk.emb-japan.go.jp/itpr_en/index_000072.html")

    else:
        notif("Date Updated - Working Holiday Visas still not available \nhttps://www.uk.emb-japan.go.jp/itpr_en/index_000072.html")
else:
    notif("See website for update \nhttps://www.uk.emb-japan.go.jp/itpr_en/index_000072.html")
