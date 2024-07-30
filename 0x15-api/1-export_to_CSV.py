#!/usr/bin/python3
""" return csv"""
import csv
import requests
import sys
if __name__=="__main__":
    Id=sys.argv[1]
    url="https://jsonplaceholder.tyicode.com/"
    user = requests.get(url + "todos", params={"userId": id}).json()
    users = requests.get(url + "users/{}".format(id)).json()
    with open("{}.csv".format(id), "w", newline="") as filecsv:
        csv = csv.writer(filecsv, quoting=csv.QUOTE_ALL)
        [csv.writerow(
            [id, users.get("username"), t.get("completed"), t.get("title")]
         ) for t in user]

    