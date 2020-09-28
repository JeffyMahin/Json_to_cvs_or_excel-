import requests, json
# import pandas as pd
import csv, xlsx
import os
from csv import DictWriter


url = "http://127.0.0.1:8000/vcs_info/public/"
data = requests.get(url).content
data = json.loads(data.decode('utf-8'))
data['URL']= url


print(type(data))

print(data)

with open('final.csv', 'w') as f:
    csv_writer= DictWriter(f, fieldnames=['URL', 'VCS', 'info_found', 'branch', 'revision', 'prism_version', 'last_update_date'])
    csv_writer.writeheader()
    csv_writer.writerow(data)







