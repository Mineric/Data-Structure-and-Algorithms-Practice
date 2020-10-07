import requests
import os
import re
import codecs

while  True:
    s = input("zip code: ")
    if not re.match(r"[0-9]{7}" ,s):
        print("Please input a zip code!")
    else:
        response = requests.get("http://zip.cgis.biz/csv/zip.php?zn={}".format(s))
        a = response.text
        print(a)
        print("postal code: ", re.sub(r'(\d{3})(\d{4})', r'\1-\2', s))
        break

os.makedirs(os.path.expanduser("~") + r"\Documents\cs_exercise\6", exist_ok = True)
with codecs.open(os.path.expanduser("~")+r"\Documents\cs_exercise\6\result.csv","w", 'utf8') as f1:
    f1.writelines(a)
    
with codecs.open(os.path.expanduser("~")+r"\Documents\cs_exercise\6\result.csv", 'r', 'utf8')as f1: # codecs.open to encode the unicode characrter
    #l = csv.reader(f1)
    kana = 0
    kanji = 0

    postal = ''
  
    r = [] 
    for row in f1:
        #print(row)
        r += row
        #print (r)
    kana_list = []
    kanji_list = []

    for i in r:
        m = re.fullmatch(r"([\u30a0-\u30ff])", i) #range of katakana character (unicode)
        if m :
            kana += 1
            kana_list.append(m.group())
            
    print ("kana: ", str(kana_list))
    print (kana, "Kana characters")

    
    for j in r:
        n = re.fullmatch(r"([\u4e00-\u9f62])", j) #range of kanji character (unicode)
        if n :
            kanji += 1
            kanji_list.append(n.group())
    
    print ("kanji: ", str(kanji_list))
    print (kanji, "Kanji characters")

    
