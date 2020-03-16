#from urllib.request import urlopen as urlRequest
#written in python 3.x
import urllib.request as urllib
from bs4 import BeautifulSoup as soup
import smtplib
import os

pathForLastSendPriceFile = "/Users/viksaa/Desktop/FINKI/codingInPython/lastSendPrice.txt"

def readPriceFromFile():
    lastSendPriceFile = open(pathForLastSendPriceFile, "r")
    price = lastSendPriceFile.read()
    lastSendPriceFile.close()
    return price
    
def updateLastSentPrice(withPrice):
    lastSendPriceFile = open(pathForLastSendPriceFile, "w+")
    lastSendPriceFile.write(withPrice)
    lastSendPriceFile.close()
    
def sendMail(withMessage):
    senderEmail = "innitibusiness@gmail.com"
    receiverEmail = "kuzmanovviktor4@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderEmail, "mnogujakpasvord123")
    print("login succesfull")
    server.sendmail(senderEmail, receiverEmail, withMessage)
    
#--------------------------------------------------------------------------------
#CHECK THE PRICE
url = "https://finance.yahoo.com/quote/TSLA/"
response = urllib.urlopen(url)
pageSoup = soup(response.read(), "html.parser")
currentTeslaPrice = float(pageSoup.findAll("span", {"class": "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"})[0].text)

response.close()

# Check if current live tesla price has changed by amount of changeInPrice value and if yes update price and send mail
# ako apsolutnata razlika mu e = ili > od changeInPrice znaci da
changeInPrice = 10.00
lastSendPrice = readPriceFromFile()

if(abs(float(lastSendPrice) - currentTeslaPrice) >= changeInPrice):
    updateLastSentPrice(str(currentTeslaPrice))
    sendMail(str(currentTeslaPrice))


