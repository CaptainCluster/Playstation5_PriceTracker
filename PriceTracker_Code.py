import PriceTracker_Parameters
import requests
from bs4 import BeautifulSoup

class SOURCE():
    def __init__(self, sourceList):
        self.name = sourceList[0]
        self.URL = sourceList[1]
        self.tag = sourceList[2]
        self.ID = sourceList[3]
        self.type = sourceList[4]
        self.classInfo = sourceList[5]
        self.title = None
        self.price = None
        return None
    
    def setupProcess(self): #Gets all the desired information and gives the information to desired variables
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id = self.ID)
        self.title = soup.find(self.tag)
        self.price = results.find(self.type, {"class", self.classInfo})
        return None

    def printInformation(self):
        print("Kauppa: " + str(self.name))
        print(self.title.text)
        print(self.price.text)
    
def main():
    for website in PriceTracker_Parameters.AllSites:
        priceSource = SOURCE(website)
        priceSource.setupProcess()
        priceSource.printInformation()

main()