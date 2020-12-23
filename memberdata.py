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


	#チャンネル取得方法確認部
	if Datas[0].find('strong').text == "主な活動場所":
		print("type_A")
		print(Datas[0].find_all("td")[1].find_all("a")[0].get("href"))
		print(Datas[0].find_all("td")[1].find_all("a")[1].get("href"))
		Datas.pop(0)
	else:
		print("お腹すいたwikiwiki")


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
			fansmark = re.search("ファンマーク(.+)", namedata).group(1)
			print(fansmark)

			print(fansmark.replace(re.search("(.*)",fansmark)).group(1).text,"")

start()