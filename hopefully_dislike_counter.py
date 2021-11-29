from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

class hopefully_sudoku:
  def __init__(self):
    self.youtube_url = ""
    self.num_likes = 0
    self.num_dislikes = 0
    self.like_to_dislike_ratio = 0.0
    self.well_liked = ""

  def webscraper(self):
    page_url = "https://grid.websudoku.com/?level=1&amp;set_id=1" # scrapes data from grid.websudoku.com

    uClient = uReq(page_url) # downloads the html page from page_url

    page_soup = soup(uClient.read(), "html.parser") # parses html into a soup data structure (readable)

    board_container = page_soup.find("form", {"name": "board"}) # narrows html down to the 'board'

    self.solved_board_num = board_container.find(attrs = {"name": "cheat"})["value"] # grabs solved numbers
    self.missing_board_num = board_container.find(attrs = {"id": "editmask"})["value"] # grabs 'missing' numbers

  def format(self):
    print("Number of likes:", self.num_likes)
    print("Number of dislikes:", self.num_dislikes)

    self.like_to_dislike_ratio = self.num_likes / self.num_dislikes
    
    print("Like to Dislike ratio:", self.like_to_dislike_ratio)
    # print("Is it a well-liked video?", )

  def run(): # welcome prompt / "user interface" on the terminal
    print("Welcome to Sudoku!")
    test = hopefully_sudoku()

    playing = True
    while (playing):
      test.webscraper()
      test.format()

      print("load another solved sudoku? y/n")
      if (str(input()) == 'n'):
        exit()
      else:
        break

loop = True # loops until player doesn't wanna play anymore
while (loop):
  hopefully_sudoku.run()