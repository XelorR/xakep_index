import csv
from bs4 import BeautifulSoup


def parse_file(issue_number: str = "261"):
    with open(f"{issue_number}.csv", "w", encoding="utf-8") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow("issue name comment".split())

        f = open(f"{issue_number}.html", "r", encoding="utf-8")
        soup = BeautifulSoup(f, "lxml")

        issue_content = soup.find("div", attrs={"id": "issue-content"})
        h3 = [e.text for e in issue_content.find_all("h3")]
        h4 = [e.text for e in issue_content.find_all("h4")]

        for i in zip(h3, h4):
            csvwriter.writerow([f"{issue_number}"] + list(i))

        f.close()


for i in [194] + list(range(211, 260)):
    print("Processing file", i)
    parse_file(str(i).zfill(3))
