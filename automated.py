# This is my automated checker which doesn't send notifications in the case of no update

import bs4
import requests

from notifypy import Notify


APP_NAME = "Website Checker"
SITE_URL = "https://www.uk.emb-japan.go.jp/itpr_en/index_000072.html"


def scrape_site(site_url: str) -> [str, str]:
    res = requests.get(site_url)
    try:
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")

        warning = soup.select_one("#main > div:nth-child(4) > div > div > div > p > font > strong").text.strip()
        last_updated = soup.select_one("#main > div:nth-child(2)").text.strip()
    except:
        pass

    if warning and last_updated:
        return warning, last_updated
    else:
        return


def main():
    target_date = "2021/7/1"
    restriction = "Due to restrictions relating to the coronavirus pandemic, we are not able to take applications for the Working Holiday Visa."

    try:
        warning, last_updated = scrape_site(SITE_URL)

        if warning == restriction:
            if last_updated == target_date:
                message = "No Update"
            else:
                message = f"Date Updated, working holiday visas still not available - see website: \n{SITE_URL}"
        else:
            message = f"See website for update: \n{SITE_URL}"
    except:
        message = f"Error - see website: \n{SITE_URL}"

    if message != "No Update":
        Notify("Japan Working Holiday Visa", message, APP_NAME).send()
    
    return message


if __name__ == "__main__":
    main()
