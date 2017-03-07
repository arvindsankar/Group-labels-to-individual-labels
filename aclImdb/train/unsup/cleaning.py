import glob
from bs4 import BeautifulSoup

files = glob.glob("*.txt")

for fi in files:
	with open(fi) as markup:
		 soup = BeautifulSoup(markup.read(), 'lxml')
	txt = soup.get_text()
	f = open(fi, 'w')
	f.write(txt.encode('utf8'))
	f.close()
	print fi