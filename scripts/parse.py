from gather import *

if __name__ == "__main__":
	f = open("../data/href.txt", "r")
	hrefs = f.read()

	href_a = hrefs.split("\n")
	href_a = href_a[:-1] #remove empty

	f.close()

	base = "https://basketball-reference.com"

	g = open("../data/scores.csv", "w")

	for idx, href in enumerate(href_a):
		#this is in a comment so.
		game = get_parsed_page(base + href_a[idx])
		table = game.find("div", {"id": "line_score_sh"})
		table = table.next_sibling.next_sibling.next_sibling
		table = BeautifulSoup(table, 'lxml')
	
		cells = table.findAll("td", {"class": "center"})

		for item in cells:
			if item["data-stat"] == "T":
				print(item.find("strong").text)
				g.write(item.find("strong").text + ",")
			else:
				print(item.text)
				g.write(item.text + ",")
		g.write("\n")
