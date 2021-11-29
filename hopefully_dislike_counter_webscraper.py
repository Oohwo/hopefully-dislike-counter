from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

page_url = "" # scrapes data from grid.websudoku.com

uClient = uReq(page_url) # downloads the html page from page_url

page_soup = soup(uClient.read(), "html.parser") # parses html into a soup data structure (readable)

board_container = page_soup.find("form", {"name": "board"}) # narrows html down to the 'board'
