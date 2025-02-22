import requests
from bs4 import BeautifulSoup  # get data from HTML , XML ==> Parser => Parsed Tree

url = "https://www.formula1.com/en/results/2024/drivers"
res = requests.get(url)
if res.status_code == 200:
    soup = BeautifulSoup(res.content, "html.parser")
    title = soup.title.text
    # get all div
    # divTags = soup.div
    # childDiv = soup.find("div", "order-1")
    table = soup.find("table", "f1-table f1-table-with-data w-full")
    rows = table.find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        if columns:
            for idx, td in enumerate(columns):
                p = td.find("p").text.strip()
                if idx == 0:
                    print(f"Pos : {p}")
                elif idx == 1:
                    print(f"Driver : {p}")
                elif idx == 2:
                    print(f"Nationality : {p}")
                elif idx == 3:
                    print(f"Car : {p}")
                elif idx == 4:
                    print(f"PTS : {p}")
