import requests
import time
from bs4 import BeautifulSoup

def get_parsed_page(url):
	headers = {
		"referer": "https://basketball-reference.com",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
	}

	time.sleep(9)

	return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

if __name__ == "__main__":
	f = open("../data/href.txt", 'w')

	h_boxes = []
	months = ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May']
	for month in months:
		print(month + "...")
		season = get_parsed_page("https://www.basketball-reference.com/leagues/NBA_2023_games-" + month.lower() + ".html")

		boxes = season.findAll("a", text="Box Score")
		
		for item in boxes:
			print(item["href"])
			f.write(item["href"] + "\n")
	f.close()

