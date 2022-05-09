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

copycat("https://studentwebsites.ccrce.ca/mj415746/index.html")

# import time
#
# def find_users_sync(n):
#     for i in range(1, n + 1):
#         print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
#         time.sleep(1)
#     print(f'> 총 {n} 명 사용자 동기 조회 완료!')
#
# def process_sync():
#     start = time.time()
#     find_users_sync(3)
#     find_users_sync(2)
#     find_users_sync(1)
#     end = time.time()
#     print(f'>>> 동기 처리 총 소요 시간: {end - start}')
#
# if __name__ == '__main__':
#     process_sync()
#
# import time
# import asyncio
#
# async def find_users_async(n):
#     for i in range(1, n + 1):
#         print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
#         await asyncio.sleep(1)
#     print(f'> 총 {n} 명 사용자 비동기 조회 완료!')
#
# async def process_async():
#     start = time.time()
#     await asyncio.wait([
#         find_users_async(3),
#         find_users_async(2),
#         find_users_async(1),
#     ])
#     end = time.time()
#     print(f'>>> 비동기 처리 총 소요 시간: {end - start}')
#
# if __name__ == '__main__':
#     asyncio.run(process_async())



# import asyncio
# import sys
# import os
# import time
# import platform
#
# result = []
#
# def getTree(search_drive):
#     return os.walk(search_drive)
#
# def pathJoin(root, filename):
#     return os.path.join(root, filename)
#
# def find_files(filename, search_path):
#    return list(pathJoin(root, filename) for root, dir, files in getTree(search_path) if filename in files)
#
# start = time.time()
# user = "ty.py"
# result = [find_files(user, f"{chr(i)}://") for i in range(ord("A"), ord("Z") + 1)]
#
# print(result)
#
# print(time.time() - start)
# """
# import os
# from math import sin, cos

# def main():
#     a=0
#     b=0

#     height=24
#     width=80
#     #height=int(input("Enter Screen Height : "))
#     #width=int(input("Enter Screen Width : "))

# 	# for clearing console (windows and unix systems)
#     clear = "cls"
#     if os.name == "posix":
#         clear = "clear"

#     os.system(clear)
#     while True:
#         z = [0 for _ in range(4*height*width)]
#         screen = [' ' for _ in range(height*width)]

#         j=0
#         while j<6.28:
#             j+=0.07
#             i=0
#             while i<6.28:
#                 i+=0.02

#                 sinA=sin(a)
#                 cosA=cos(a)
#                 cosB=cos(b)
#                 sinB=sin(b)

#                 sini=sin(i)
#                 cosi=cos(i)
#                 cosj=cos(j)
#                 sinj=sin(j)

#                 cosj2=cosj+2
#                 mess=1/(sini*cosj2*sinA+sinj*cosA+5)
#                 t=sini*cosj2*cosA-sinj* sinA

#                 # 40 is the left screen shift
#                 x = int(40+30*mess*(cosi*cosj2*cosB-t*sinB))
#                 # 12 is the down screen shift
#                 y = int(11+15*mess*(cosi*cosj2*sinB +t*cosB))
#                 # all are casted to int, ie floored
#                 o = int(x+width*y)
# 				# multiplying by 8 to bring in range 0-11 as 8*(sqrt(2))=11
# 				# because we have 11 luminance characters
#                 N = int(8*((sinj*sinA-sini*cosj*cosA)*cosB-sini*cosj*sinA-sinj*cosA-cosi *cosj*sinB))
# 				# if x,y inside screen and previous z-buffer is < mess
# 				# i.e. when z[o] is 0 or the prev point is behind the new point
# 				# so we change it to the point nearer to the eye/ above prev point
#                 if 0<y<height and 0<x<width and z[o] < mess:
#                     z[o]=mess
#                     screen[o]=".,-~:;=!*#$@"[N if N>0 else 0]

#         # prints
#         os.system(clear)
#         for index, char in enumerate(screen):
#             if index % width == 0:
#                 print()
#             else:
#                 print(char, end='')

#         # increments
#         a+=0.04
#         b+=0.02

# if __name__ == "__main__":
#     main()
# """
