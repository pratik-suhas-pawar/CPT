import requests
from datetime import datetime


class GitData:
    def __init__(self):
        date, month_year = str(int(datetime.now().strftime("%d"))), datetime.now().strftime("%B %Y").split(" ")
        self._today = month_year[0] + " " + date + ", " + month_year[1]
        print(self._today)

    def get_today(self, usr_id: str = "") -> "Returns today's report":
        data = str(requests.get(f"https://www.github.com/{usr_id}").content)
        find_index = data.find(self._today)
        contrib = str(data)[find_index - 35: find_index + 13].split(">")[-1].split(" ")[0]
        if contrib == "NO":
            return 0

# print(GitData().get_today(usr_id="pratik-suhas-pawar"))
