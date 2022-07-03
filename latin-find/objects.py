import requests
from bs4 import BeautifulSoup 
import re 

class latinFind():
    def __init__(self):
        self.parolaLink = "https://www.online-latin-dictionary.com/latin-english-dictionary.php?parola="
        self.lemmaLink = "https://www.online-latin-dictionary.com/latin-english-dictionary.php?lemma="

        

    def getSoup(self, latinword): 
        response = requests.get(f"{self.parolaLink}{latinword}").text 
        soup = BeautifulSoup(response, 'html.parser')
        return soup 

    # The default translation reqest 
    def reqDefault(self, word): 
        translationList = []
        disambigua = []
        soup = self.getSoup(word)
        disambiguation = soup.find("ul", attrs={"class": "disambigua"})
        
        if disambiguation: 
            translationList.append(disambiguation.text)
            tags = disambiguation.find_all("a")
            print(tags)
            #href = tags["href"]
            #m = re.search(r'\b=(\w+)', href)
            #tref = m.group(1)

            

        translation = soup.find("div", attrs={"id": "myth"})
        if translation:
            transList = translation.find_all("span", attrs={"class": "english"})
            latinType = translation.find("span", attrs={"class": "grammatica"}).text

            translationList.append(latinType)
            for trans in transList: 
                translationList.append(trans.text) 

            self.formatPrint(translationList)

        return disambigua, translationList 

    def reqLemma(self): 
        pass 

    def formatPrint(self, listObj):
        for j, line in enumerate(listObj): 
            print(f"{j+1}: {line}")


            

l1 = latinFind()

print(l1.reqDefault("ab"))