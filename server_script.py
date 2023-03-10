from datetime import datetime
import requests
import time

cnt = 0
date_prev, month_year_prev = str(int(datetime.now().strftime("%d"))), datetime.now().strftime("%B %Y").split(" ")

while 1:
    print("prev_date: ", date_prev)

    if (date_prev != str(int(datetime.now().strftime("%d"))) and month_year_prev != datetime.now().strftime("%B %Y").split(" ")) or cnt == 0:
        cnt = 1
        print("running")
        date, month_year = str(int(datetime.now().strftime("%d"))), datetime.now().strftime("%B %Y").split(" ")
        log_data = []
        log_data.append(month_year[0] + " " + date + ", " + month_year[1])
        git_usr_id = ["pratik-suhas-pawar", "mr-vicky", "Prasadcode22", "Sanketkatkade"]

        for usr_id in git_usr_id:

            data = str(requests.get(f"https://www.github.com/{usr_id}").content)
            find_index = data.find(month_year[0] + " " + date + ", " + month_year[1])
            print(str(data)[find_index - 30: find_index + 13])
            log_data.append(usr_id + "->" + str(data)[find_index - 30: find_index + 13] + "|")

        with open("log.csv", "w") as log:
            for i in log_data:
                log.write(i)

        date_prev, month_year_prev = str(int(datetime.now().strftime("%d"))), datetime.now().strftime("%B %Y").split(" ")

    # if input("Type and Enter 'exit' or 'quit' to exit: ") == "q" or "e" or "quit" or "exit":
    #     break
    time.sleep(1)
