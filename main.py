# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:45:31 2021
@author: Marlou
Задача получить код текст с web-страницы и найти на нём информацию, а также ссылки и находящуюся на них информацию до n-ого порядка
Актуальная информация о сборке :
    -Выключек поиск и вывод абсолютных ссылок
    -Примерные ссайты для проверки работоспособности : 'https://yummyanime.club/top' 'https://www.avito.ru/sankt-peterburg' 'https://yummyanime.club/top' 'https://pythonworld.ru/osnovy/vozmozhnosti-yazyka-python.html' 'https://pythonworld.ru/bookshop' 'https://pythonworld.ru/osnovy/vozmozhnosti-yazyka-python.html'
    -
"""
import urllib.request
import numpy as N


class Data:  # Класс данных
    strURL: str  # Ссылка на сайт
    strWebCode: str
    strText = ''
    staticMainURL = ''
    listConditionalNetLinks = []
    listAbsoluteNetLinks = []
    listAllConditionalNetLinks = []
    listUsedConditionalNetLinks = []
    intActualDepthLevel = 0
    intActualintObjectsCount = 0
    staticintDepthLevel = 2
    staticintCountOfPagesOnLevel = 3

    def __init__(self, strURL):  # Конструктор первого объекта
        self.strURL = strURL  # Передаём объекту класса ссылку на сайт
        if Data.intActualintObjectsCount == 0 : Data.getMainURL(self)
        self.getWebCode()
        self.getText()
        self.getNetLinks()
        self.printObjectInfo()
        self.makeNewFile()
        self.makeNewData()

    def printObjectInfo(self):
        print('-' * 30)
        print("1. Objects count -", self.intActualintObjectsCount)
        print("2. Main URL -", self.staticMainURL)
        print("3. Depth level -", self.intActualDepthLevel)
        print("4. URL -", self.strURL)  # Ссылка на сайт
        print('-' * 30)

    def makeNewData(self):
        while Data.intActualDepthLevel != Data.staticintDepthLevel + 1:
            self.listConditionalNetLinks = [i for i in self.listConditionalNetLinks if not i in Data.listUsedConditionalNetLinks]
            Data.intActualintObjectsCount += 1
            intNumOfPagesOnLevel = Data.intActualintObjectsCount % Data.staticintCountOfPagesOnLevel
            if intNumOfPagesOnLevel == (Data.staticintCountOfPagesOnLevel - 1):
                Data.intActualDepthLevel += 1
            else:
                Data.listUsedConditionalNetLinks.append(self.listConditionalNetLinks[intNumOfPagesOnLevel])
                Data(Data.staticMainURL + self.listConditionalNetLinks[intNumOfPagesOnLevel])

    def makeNewFile(self):
        strFileName =  r"C:\Users\misha\Documents\URL" + str(self.intActualintObjectsCount) + ".txt"# Создаём уникальную ссылку на файл и записываем её в соотв. поле
        with open(strFileName, 'w') as fileNewFile: # Открываем файл
            typleLine = '-' * 30 + '\n 1. Objects count -', str(self.intActualintObjectsCount) + "\n 2. Main URL -", str(self.staticMainURL) + "\n 3. Depth level -", str(self.intActualDepthLevel) + "\n 4. URL -", self.strURL + "\n 5. Conditinal links -"
            strLine = ''.join(typleLine)
            fileNewFile.write(strLine)
            for i in range(len(self.listConditionalNetLinks)):
                fileNewFile.write(''.join("  " +self.listConditionalNetLinks[i]))
            fileNewFile.write('\n Text - ')
            for i in range(len(self.strText)):
                fileNewFile.write(self.strText[i])
            fileNewFile.write('-'*30)
        
    def getWebCode(self):  # 1 Исправна
        strWebCode = ''  # Создаём пустую строку
        tupleRequest = urllib.request.Request(self.strURL, data=None, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        with urllib.request.urlopen(tupleRequest) as bityNetCode:  # Получаем код web-страници
            listLines = bityNetCode.readlines()  # Переписываем его в список строк
            for i in range((len(listLines))):  # Начинаем цикл по количеству строк
                try:
                    strWebCode += listLines[i].decode(
                        'utf-8')  # Расшифровываем строку из unicode в utf-8 и записываем её в строку
                except Exception:
                    pass
        self.strWebCode = strWebCode  # Возвращаем строку

    def getMainURL(self):
        intSlashCounter = 0
        for i in range(len(self.strURL)):
            if self.strURL[i] == '/' and intSlashCounter != 3:
                intSlashCounter += 1
            elif intSlashCounter == 3:
                break
            Data.staticMainURL += self.strURL[i]

    def isRussianChar(strCharToComparison):  # Функция нахождения русского символа в коде страници # Исправна
        intChar = ord(
            strCharToComparison.upper())  # Присваеваем переменной код символа по таблице ASCII предворительно превидя сивол к верхнему регистру
        if 1040 <= intChar <= 1071 or intChar == 1025 or intChar == 1105:  # Проверяем является символ символом русского алфавита
            return True  # Да
        return False  # Нет

    def getText(self):  # 2 Исправна
        boolFlag = False
        for i in range(1, len(self.strWebCode)):
            if Data.isRussianChar(self.strWebCode[i]) and boolFlag == False:
                boolFlag = True
            elif (self.strWebCode[i] == '<' or self.strWebCode[i] == '>' or self.strWebCode[i] == '"' or
                  self.strWebCode[i] == '&' or self.strWebCode[i] == '=') and boolFlag == True:
                boolFlag = False
                self.strText += ' '
            if boolFlag:
                self.strText += self.strWebCode[i]

    def getNetLinks(self):
        intIndex = 0  # Создаем переменню отвечающую за шаг в цикле while
        while self.strWebCode.find('href=', intIndex, len(self.strWebCode)) != -1:
            intIndex = self.strWebCode.find('href=', intIndex, len(self.strWebCode))
            i = 5
            strLink = ''
            while self.strWebCode[intIndex + i] != '<' and self.strWebCode[intIndex + i] != '>' and self.strWebCode[intIndex + i] != ' ' and self.strWebCode[intIndex + i] != '?':
                strLink += self.strWebCode[intIndex + i]
                i += 1
            strLink = strLink.replace('"', '')
            if strLink[0] == '/':
                self.listConditionalNetLinks.append(strLink[1:len(strLink)])
            else:
                self.listAbsoluteNetLinks.append(strLink)
            intIndex += len(strLink) + len('href=')

        self.listConditionalNetLinks = N.unique(N.array(self.listConditionalNetLinks)).tolist()
        Data.listAllConditionalNetLinks += N.setdiff1d(self.listConditionalNetLinks, Data.listAllConditionalNetLinks).tolist()
        self.listAbsoluteNetLinks = N.unique(N.array(self.listAbsoluteNetLinks)).tolist()

def main():
    strURL = 'https://yummyanime.club/top'
    dataObject = Data(strURL)
    input("Press Enter to continue...")

main()