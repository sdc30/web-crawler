## Cartwright, Stephen D
## 8/11/16

import requests

class Saver():
	
	
	
	def __init__(self):
		self.url = ''
		self.html = ''
		
	def proc(self):
		res = requests.get(self.url)
		self.html = self.url.split("/")[-1]
		try:
			res.raise_for_status()
		except Exception as exc:
			print "Problem: %s" % exc
			
		#page = bs4.BeautifulSoup(res.text, 'html.parser')
		#(NO) page = bs4.BeautifulSoup(res.text)

		if res.status_code == requests.codes.ok:
			#print "OK"
			f = open(self.html, 'wb')
			for chunk in res.iter_content(100000):
				f.write(chunk)
			f.close
		else:
			print "Not OK ----- "
			
			
			
	def main(self, url):
		#url = 'http://www.cse.psu.edu/~deh25/cmpsc311/Lectures/'
		self.url = url
		
		self.proc()


#exe = save()
#exe.main()
