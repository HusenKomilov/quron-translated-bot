import requests


url1 = requests.get("https://api.quran.com/api/v4/chapters?language=uz")

text1 = url1.json()
chapters = text1['chapters']


url2 = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json")
text2 = url2.json()
verse = text2['quran']
