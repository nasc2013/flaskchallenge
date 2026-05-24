import requests
from bs4 import BeautifulSoup

def extract_web3_jobs(keyword):
    url = f"https://web3.career/{keyword}-jobs"
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("tr", class_="table_row")

    result = []
    for i in jobs:
        title_div = i.find("div", class_="job-title-mobile")
        company_td = i.find("td", class_="job-location-mobile")
        if not title_div or not company_td:
            continue
        if not title_div.find("h2") or not company_td.find("h3"):
            continue
        title = title_div.find("h2").text.strip()
        company = company_td.find("h3").text.strip()
        link = "https://web3.career" + title_div.find("a")["href"]
        result.append({
            "position": title,
            "company": company,
            "link": link
        })
    return result