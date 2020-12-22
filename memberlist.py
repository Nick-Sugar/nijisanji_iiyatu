#import requests
from bs4 import BeautifulSoup
import urllib.request
import lxml.html


def start():
	r = urllib.request.urlopen("https://nijisanji.ichikara.co.jp/member/")
	test2 = lxml.html.fromstring(r.read())

	for i in range(1, len(test2.xpath(f'//*[@id="liver_list"]/div')) + 1):
		datas = test2.xpath(f'//*[@id="liver_list"]/div[{i}]/div/div/a/span')
		print(datas[0].text.replace("\n",""))

start()