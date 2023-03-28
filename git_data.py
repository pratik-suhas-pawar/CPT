import requests
from datetime import datetime


class GitData:
    def __init__(self):
        date, month_year = str(int(datetime.now().strftime("%d"))), datetime.now().strftime("%B %Y").split(" ")
        self._today = month_year[0] + " " + date + ", " + month_year[1]
        print(self._today)

    

# print(GitData().get_today(usr_id="pratik-suhas-pawar"))
