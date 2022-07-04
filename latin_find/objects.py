import requests
import logging 
from bs4 import BeautifulSoup 
import re 

logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class latinFind():
    '''Class API for online latin dictionary'''
    def __init__(self):
       pass 

    def getSoup(self, link, latinword): 
        '''Gets the soup of the page with the a specific latin word translated to english'''
        response = requests.get(f"{link}{latinword}").text 
        logging.debug(f"{link}{latinword}")
        soup = BeautifulSoup(response, 'html.parser')
        return soup 


    def formatDisambigua(self, listObj, taglist):
        '''Prints out the disambigua in prettier format'''
        for i, dis in enumerate(listObj):
            if "IN THIS PAGE" in dis: 
                new = dis.split("IN THIS PAGE")
                print(f"{new[0]} [CURRENT]")
            else: 
                print(f"{dis} [WORD TAG: {taglist[i]}]")


    def formatPrint(self, listObj):
        '''Prints out the translation list in prettier format'''
        print(f"\nGrammar: {listObj[0]}")
        for j, line in enumerate(range(1, len(listObj))): 
            print(f"{line}: {listObj[line]}")


    def reqDefault(self, link, word):
        '''The default translation page with parola keyword at the end of URL''' 
        translationList = []
        soup = self.getSoup(link, word)

        # finding possible alternative translations to the word 
        disambiguation = soup.find("ul", attrs={"class": "disambigua"})
        if disambiguation: 
            taglist = []
            disambigtext = disambiguation.text 
            disambigList = disambigtext.split("\n")
            disambigList.pop(0)
            disambigList.pop()

            tags = disambiguation.find_all("a")
        
            for tag in tags: 
                href = tag["href"]
                s = re.split(r'=', href)
                taglist.append(s[-1]) 

            self.formatDisambigua(disambigList, taglist)
            
        # listing out all the translations of the word     
        translation = soup.find("div", attrs={"id": "myth"})
        if translation:
            transList = translation.find_all("span", attrs={"class": "english"})
            latinType = translation.find("span", attrs={"class": "grammatica"}).text

            translationList.append(latinType)
            for trans in transList: 
                translationList.append(trans.text) 

            self.formatPrint(translationList)
        # If there are only results instead of a direct translation (using omnipotenti as an example)
        else: 
            td = soup.find("td", attrs={"id": "middle"})
            table = td.find("table", attrs={"width": "100%"})
            tr = table.find_all("tr") 
            print(tr)
            



            

