import csv
from bs4 import BeautifulSoup


def parse_file(issue_number: str = "193"):
    f = open(f"html/{issue_number}.html", encoding="utf-8")

    soup = BeautifulSoup(f, "lxml")
    issue_content = soup.find("div", attrs={"id": "issue-content"})
    content = [e.text.split(". ", 1) for e in issue_content.find_all("li")]

    with open(f"csv/{issue_number}.csv", "w", encoding="utf-8") as c:
        csvwriter = csv.writer(c)
        csvwriter.writerow("issue name content".split())
        for i in content:
            csvwriter.writerow([f"{issue_number}"] + i)

    f.close()


for i in list(range(1, 194)) + list(range(195, 211)):
    print("Processing file", i)
    parse_file(str(i).zfill(3))
