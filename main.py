# urllib is important to open a url, get code, read it etc
# json the format of data, so importing json is important
import urllib.request
import json
# Function that take symbol (stock) as input and download the data
def connectionJson(stock):
    urlData = "https://query1.finance.yahoo.com/v7/finance/quote?symbols="+stock
    # visit the web page and open the urlData
    webUrl = urllib.request.urlopen(urlData)
    # handling the errors if occurs when oppening the url
    if(webUrl.getcode() == 200):
        data = webUrl.read()
    else:
        print("Erreur du serveur : " + str(webUrl.getcode()))
    # read the content of the url and load it to a dataJson variable using the lib json.
    dataJson = json.loads(data)
    # returning data for stock wanted
    return dataJson["quoteResponse"]["result"][0]
# we ask the user to enter the data, if is lowerCase, its automatically converted to upperCase
symbolInput = input("Symbol : ")
symbolInput = symbolInput.upper()
# create the fields needed with key:value into a dictionnary
fields = {'shortName': 'Company', 'regularMarketPreviousClose': 'Close'}
result = {}
# loop that will connect to website, load data, and then put data into result
for ticker in symbolInput:
    tickerData = connectionJson(symbolInput)
    singleResult = {}
    for key in fields.keys():
        if key in tickerData:
            singleResult[fields[key]] = tickerData[key]

        else:
            singleResult[fields[key]] = "N/A"
    result[ticker] = singleResult


# print(singleResult)
# we print the company name, i know it's not asked but more meaningful
print("Company name : "+singleResult["Company"])
# prininf the previous close price as asked. If im not wrong
print("Previous Close Price  : " + str(singleResult["Close"]))
