# This is my manual checker which always sends notifications

import bs4
import requests

from notifypy import Notify
from whv_automated import APP_NAME, SITE_URL, main

main()

if main() == "No Update":
    Notify("Japan Working Holiday Visa", main(), APP_NAME).send()
