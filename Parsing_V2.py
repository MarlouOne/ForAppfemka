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

    def getClassContentCSV(self, strTagName ,strClassName,strPath = r'C:\Users\misha\Documents\parsing.csv'):
        soupTitle = self.soup.find_all(strTagName, class_= strClassName)
        for element in soupTitle:
            a = element.text
            listInfo = data.getContentList(element.text)
            data.makeCSVFile(strPath, listInfo)
            # print(listInfo)
            data.makeTextFile(listInfo)
   
    def getContetFromNextWebs(intDepth,strURL,strTagName, strClassName):
        for i in range(intDepth):
            dataObj = data(strURL+str(i))
            dataObj.getClassContentCSV(strTagName, strClassName)
            time.sleep(0.5)                
                
    def getAllNewLineInList(strText):
        listNewLinePlace = [0]    
        intLineCount = 0
        index = 0
        while intLineCount != 5:
            index = strText.find('\n', index+1, len(strText))
            listNewLinePlace.append(index)
            intLineCount += 1
        # print('\n',listNewLinePlace)
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
            # File.write('\n')

    def makeCSVFile(strPath,listInfo):
        with open(strPath, 'a+', encoding='utf-8') as File:
            writer = csv.writer(File, delimiter = ",", lineterminator="\r")
            writer.writerows(listInfo)
        
    def getAllHref(self):
        for i in self.soup.find_all('a', href=True):
            self.listConditionalNetLinks.append(i['href'])
    
    def printObjectInfo(self):
        print(self.soup)
        print(self.listConditionalNetLinks)
 
def main():    
    print(' '*6 +'PROGRAMM START WORK\n' + '-'*30)
    
    # strURL = "https://www.habr.com/"
    # strTagName = 'a'
    # strClassName = "post__title_link"
    
    strURL = 'https://www.speedguide.net/port.php?port='
    strTagName = 'tr'
    strClassName = "port"
    intDepth = 5
    
    # strPath = r'C:\Users\misha\Documents\parsing.xlsx'
    # strPath = r'C:\Users\misha\Documents\parsing.csv'
    
    # dataObj = data(strURL)
    # dataObj.getClassContentXLSX(strTagName, strClassName)
    # dataObj.getClassContentCSV(strTagName, strClassName)
    
    data.getContetFromNextWebs(intDepth,strURL,strTagName,strClassName)
    
    # dataObj.getAllHref()
    
    print('-'*30+'\n'+' '*6 +'PROGRAMM END WORK')
    
main()

