import requests
from bs4 import BeautifulSoup 
import re 

class latinFind():
    def __init__(self):
        self.parolaLink = "https://www.online-latin-dictionary.com/latin-english-dictionary.php?parola="
        self.lemmaLink = "https://www.online-latin-dictionary.com/latin-english-dictionary.php?lemma="

        self.translationList = []

    def getSoup(self, latinword): 
        response = requests.get(f"{self.parolaLink}{latinword}").text 
        soup = BeautifulSoup(response, 'html.parser')
        return soup 

    # The default translation reqest 
    def reqDefault(self, word): 
        soup = self.getSoup(word)
        disambiguation = soup.find("ul", attrs={"class": "disambigua"})
        if disambiguation: 
            tags = disambiguation.find("a")
            href = tags["href"]
            m = re.search(r'\b=(\w+)', href)
            tref = m.group(1)
            

        translation = soup.find("div", attrs={"id": "myth"})
        transList = translation.find_all("span", attrs={"class": "english"})
        latinType = translation.find("span", attrs={"class": "grammatica"}).text

        self.translationList.append(latinType)
        for trans in transList: 
            self.translationList.append(trans.text) 

        return self.translationList 

    def reqLemma(self): 
        pass 

    def formatPrint(self, listObj):
        pass  

            

l1 = latinFind()

print(l1.reqDefault("hodie"))