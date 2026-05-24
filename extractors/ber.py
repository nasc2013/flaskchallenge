import requests
from bs4 import BeautifulSoup

def extract_ber_jobs(keyword):
    url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("li", class_="bjs-jlid")

    result = []
    for i in jobs:
        title = i.find("h4", class_="bjs-jlid__h").find("a").text
        company = i.find("a", class_="bjs-jlid__b").text
        link = i.find("h4", class_="bjs-jlid__h").find("a")["href"]
        result.append({
            "position": title,
            "company": company,
            "link": link
        })
    return result