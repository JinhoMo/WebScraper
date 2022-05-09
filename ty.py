# import requests
# from bs4 import BeautifulSoup

# url = 'https://staffwebsites.ccrce.ca/belliveaud/index.html'



import requests
from bs4 import BeautifulSoup
import os

class copycat:
    def __init__(self, url : str) -> None:
        """Start of copycat

        Args:
            url (str): Input initial home page url
        """
        self.url = []
        self.url.append(url)
        self.used = []
        
        while True:
            try:
                sub = self.url[-1]
            except Exception:
                break
            
            response = requests.get(sub)
            self.used.append(sub)
            self.current = sub
            self.url[::-1].remove(sub)
            
            # if not ".html" in self.current:
                
            
            if response.status_code == 200:
                self.html = response.text
                self.soup = BeautifulSoup(self.html, 'html.parser')
                self.findUrls()
                self.findUrls("img", "src")
                self.save(self.html, os.getcwd(), self.fileName(self.current))
                print("?")
                break
            else:
                print(f"error : {response.status_code}")
                
            
    def fileName(self, url):
        return url.split("/")[-1]
    
    def requester(self):
        self.soup.get   

# f = open('NASA2.jpg','wb')
# f.write(urllib.request.urlopen('http://www.python.org/images/success/nasa.jpg').read())
# f.close()
# print("download successful")
        

    def findUrls(self, tag = "a", pro = "href"):
        tags = self.soup.find_all(tag)
        for i in tags:
            if pro in i.attrs.keys():
                self.url.append(i[pro])
        
    def save(self, data : bytes, *name:tuple) -> None:
        with open("/".join(name), "w") as file:
            file.write(data)

copycat("http://cec.ccrce.ca/")
