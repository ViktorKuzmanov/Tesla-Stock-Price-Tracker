#from urllib.request import urlopen as urlRequest
#THIS SCRIPT IS WRITTEN IN PYTHON 2.X
import urllib
from bs4 import BeautifulSoup as soup
import smtplib
import urllib2

#--------------------------------------------------------------------------------
#CHECK THE PRICE
url = "https://finance.yahoo.com/quote/TSLA/"
response = urllib2.urlopen(url)
#response = urllib.request.urlopen(url)
pageSoup = soup(response.read(), "html.parser")
teslaPrice = pageSoup.findAll("span", {"class": "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"})[0].text

senderEmail = "innitibusiness@gmail.com"  # ToSendAndReceive email - it is the same
receiverEmail = "kuzmanovviktor4@gmail.com"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderEmail, "mnogujakpasvord123")
print("login succesfull")
message = teslaPrice
server.sendmail(senderEmail, receiverEmail, message)

response.close()

