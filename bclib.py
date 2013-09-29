 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # Lucas Daltro<lucasdaltro5@gmail.com> wrote this file. As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return
 #Lucas Daltro
 # ----------------------------------------------------------------------------

import urllib2
from bs4 import BeautifulSoup


def getTaxa():
	response = urllib2.urlopen('https://www3.bcb.gov.br/ptax_internet/consultarUltimaCotacaoDolar.do')
	soup = BeautifulSoup(response)
	for dado in soup.find_all('td'):
		p = dado.get_text()
		
 	z = ""
 	s = list(p)
 	s[1] = '.'
 	for i in s:
 		z += i
 		
 	resul = float (z)
 	return resul  	
