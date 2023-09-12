import requests
from bs4 import BeautifulSoup


def extract_links(url_list) -> list:
    urls = []

    for url in url_list:
        reqs = requests.get(url)
        content = reqs.text
        soup = BeautifulSoup(content, "html.parser")

        for h in soup.findAll("td"):
            a = h.find("a")
            try:
                if "href" in a.attrs:
                    url = a.get("href")
                    urls.append(url)
            except:
                pass

    urls = [x for x in urls if "data" in x]
    urls = [x for x in urls if "_SPS" not in x]
    urls = [x for x in urls if "_Stata" not in x]
    urls = [x for y in urls for x in y.split("/")]
    urls = [x for x in urls if "data" not in x]

    urls = list(set(urls))
    return urls
