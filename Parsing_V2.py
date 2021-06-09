# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:08:09 2021
'http://www.auction.spb.ru/'

'https://www.speedguide.net/port.php?port=' -  table class="port-outer" или tr class="port"

"https://www.habr.com/" - a class_="post__title_link"
@author: Marlou
"""

# import pandas as PD
import time
import requests as R
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
import csv


class data:
    strURL : str
    soup : None
    listConditionalNetLinks = []
    
    def __init__(self, strURL):
        self.strURL = strURL
        self.getSoup()
        
    def getSoup(self):
        response = R.get(self.strURL, headers={'User-Agent': UserAgent().chrome})
        self.soup = BS(response.content, "html.parser")

    def getClassContent(self, strTagName ,strClassName,strPath = r'C:\Users\misha\Documents\parsing.csv'):
        soupTitle = self.soup.find_all(strTagName, class_= strClassName)
        for element in soupTitle:
            listInfo = data.getContentList(element.text)
            data.makeCSVFile(strPath, listInfo)
            data.makeTextFile(listInfo)
   
    def getContetFromNextWebs(intDepth,strURL,strTagName, strClassName):
        for i in range(intDepth):
            try:
                dataObj = data(strURL+str(i))
            except Exception :
                print(f"Порт {i} не существует !")
            else:
                print(f"Порт {i} обработан !")
                dataObj.getClassContent(strTagName, strClassName)
                time.sleep(0.5)                
                
    def getAllNewLineInList(strText):
        listNewLinePlace = [0]    
        intLineCount = 0
        index = 0
        while intLineCount != 5:
            index = strText.find('\n', index+1, len(strText))
            listNewLinePlace.append(index)
            intLineCount += 1
        return listNewLinePlace
        
    def getContentList(strText):
        listInfo = []
        listNewLinePlace = data.getAllNewLineInList(strText)
        for i in range(len(listNewLinePlace)-1):
            line = strText[listNewLinePlace[i]:listNewLinePlace[i+1]]
            listInfo.append(line)
        return listInfo        

    def makeTextFile(listInfo):
        with open(r'C:\Users\misha\Documents\parsing.txt', 'a+') as File:
            for i in range(len(listInfo)):
                File.write(listInfo[i])
    
    def makeFileHeadline(strPath = r'C:\Users\misha\Documents\parsing.csv',listHeadline = ["Port(s)", "Protocol","Service","Details","Source"]):
        with open(strPath, 'w', newline='') as File:
            writer = csv.writer(File, delimiter=';')
            writer.writerow(listHeadline)

    def makeCSVFile(strPath,listInfo):
        with open(strPath, 'a+', newline='') as File:
            writer = csv.writer(File, delimiter=';')
            writer.writerow(listInfo)

        
    def getAllHref(self):
        for i in self.soup.find_all('a', href=True):
            self.listConditionalNetLinks.append(i['href'])
    
    def printObjectInfo(self):
        print(self.soup)
        print(self.listConditionalNetLinks)
 
def main():    
    print(' '*6 +'PROGRAMM START WORK\n' + '-'*30)    

    strURL = 'https://www.speedguide.net/port.php?port='
    strTagName = 'tr'
    strClassName = "port"
    intDepth = 5
    
    data.makeFileHeadline()
    data.getContetFromNextWebs(intDepth,strURL,strTagName,strClassName)
    strClassName = "port-outer"
    data.getContetFromNextWebs(intDepth,strURL,strTagName,strClassName)
    
    print('-'*30+'\n'+' '*6 +'PROGRAMM END WORK')
    
main()

