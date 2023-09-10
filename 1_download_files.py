import asyncio

from config import config
from src.donwload import download
from src.parse_table import extract_links

""" this script downloads and unzips all the survey data files from IPEDS website.
All the configuration parameters are in the config file. Downloaded files are in the
'uzipped' folder.
"""

# let's prepare a list of addresses that need to be processed
page_urls = [f"{config.base_url}{year}" for year in config.years]

links = extract_links(page_urls)

links = [f"{config.data_url}{link}" for link in links]

# now, let's download asynchronously into unzipped folder
asyncio.run(download(links))
