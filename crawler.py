## Cartwright, Stephen D
## 8/11/16

import requests, bs4, urllib2
from save import Saver

class Crawler():
	

	
	def __init__(self):
		self.page = ''
		#self.url = 'http://www.cse.psu.edu/~deh25/cmpsc311/Lectures/'
		self.link_temp = ''
		self.goto_links = []
		self.final_links = []

		
		
		
	def pageSet(self, url):
		self.page = page = requests.get(url)
		#print self.page.status_code
		#print url
		page_parsed = bs4.BeautifulSoup(page.text, 'html.parser')
		ele = page_parsed.select('a')
		#print ele
		return ele
		
	def retrieve(self, ele_list, flip):
		i = 0
		exit_code = True
		length = len(ele_list)
		#u = self.goto_links[i]
		while i < length:

			try:
				e = ele_list[i].attrs.get('href')
				
				enc = e.encode("utf-8")
				
				#print enc
				if flip:
					link = self.url + enc
				else:
					link = self.link_temp + enc
				l = list(enc)
				
				
				length_l = len(l)
				
				if l.index('/') == length_l-1:
					self.goto_links.append(link)
					exit_code = False
					#print link
					
			except Exception as exc:
				self.final_links.append(link)
				#print link
				#print self.url+enc
				#r = requests.get(self.url+enc)
				#if r.status_code == requests.codes.ok:
				#print ''

				
			i = i + 1
		return exit_code
	
	
	def link_setup(self, ele_list):
		print ''
			
		
	def page_jumper(self):
		i = 0
		l = len(self.goto_links)
		exit_code = False
		
		while i < l:
		
			#print self.goto_links[i]
			self.link_temp = self.goto_links[i]
			#print self.link_temp
			e = self.pageSet(self.goto_links[i])
			exit_code = self.retrieve(e, 0)
			#print self.goto_links
			#print self.final_links
			#self.goto_links = []
			i = i + 1
			
			
		return exit_code
		
	def proc(self):
		processor = Saver()
		for l in self.final_links:
			#print l
			processor.main(l)

		
	def main(self, url):
		#self.url = 'http://www.cse.psu.edu/~deh25/cmpsc311/Lectures/'
		#self.url = 'http://www.cse.psu.edu/~deh25/cmpsc473/notes/'
		self.url = 'http://www.cse.psu.edu/~deh25/cmpsc461/notes/'
		e = self.pageSet(self.url)
		self.retrieve(e, 1)
		
		#elems = self.pageSet(self.url)

		#
		#exit_code = False
			
		while True:
			exit_code = self.page_jumper()
			if exit_code is True:
				break
		
		
		self.proc()
		
		


exe = Crawler()
exe.main(raw_input('Start URL > '))

