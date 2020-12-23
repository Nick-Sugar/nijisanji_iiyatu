from bs4 import BeautifulSoup
import requests
import re


def start():
	r = requests.get("https://wikiwiki.jp/nijisanji/"+"える");
	d = BeautifulSoup(r.text, "html.parser")
	Overall = d.find_all('div',class_ = 'h-scrollable')[0]
	Datas = Overall.find_all('tr')
	#print(Overall)
	#print(len(Datas))
	Datas.pop(0)
	Datas.pop(-1)
	i = 0
	for Data in Datas:
		i = i+1
		print(Data.find('strong').text + "  *"+ str(i)+"番目")
		if Data.find('strong').text == "ハッシュタグ":
			for tag in Data.find_all("td")[1].find_all("a"):
				print(tag.text)
		if Data.find('strong').text == "ファンの呼称等":
			namedata =Data.find_all("td")[1].text
			print(Data.find_all("td")[1].text)
			print(re.search("ファンの呼称：.*ファンマーク",namedata).group().replace("ファンの呼称：","").replace("ファンマーク",""))
			print(re.search("ファンマーク.+", namedata))


	#チャンネル取得方法確認部
	if Datas[1].find('strong').text == "主な活動場所":
		print("type_A")
start()