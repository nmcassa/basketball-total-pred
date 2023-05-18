from gather import *

if __name__ == "__main__":
	f = open("../data/teams.csv", 'w')

	h_boxes = []
	months = ['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May']
	for month in months:
		print(month + "...")
		season = get_parsed_page("https://www.basketball-reference.com/leagues/NBA_2023_games-" + month.lower() + ".html")

		away = season.findAll("td", {"data-stat": "visitor_team_name"})
		home = season.findAll("td", {"data-stat": "home_team_name"})
		
		for idx, item in enumerate(away):
			#print(away[idx].find("a").text)
			#print(home[idx].find("a").text)\
			f.write(away[idx].find("a").text + "," + home[idx].find("a").text + "\n")
	f.close()