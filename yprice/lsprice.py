import json
import sys
import yfinance as yf

num_col_size:float  = 8.0

foreColors = {
    "red" : "31"
    ,"green" : "32"
}

def getColorByKey(sKey:str):
    if(sKey == ""):
        return foreColors[sKey]
    elif(sKey == ""):
        return ""

def getStrPaddding(col:dict,sVal:str):
    iAlign:int = 0
    iWidth:int  = col["width"]
    colorCode : str = "0"

    if "align" in col:
        iAlign = col["align"]
    
    if(iAlign == 0):
        return sVal.ljust(iWidth)
    elif iAlign == 1:
        return sVal.rjust(iWidth)
    elif iAlign == 2:
        return sVal.center(iWidth)

def printHeader(grid):

    iCount:int = 0
    for _col in grid["cols"]:
        sColTitle = getStrPaddding(_col,_col["title"])
        iCount += _col["width"] + 1
        print(sColTitle,end="|")
        
    print("")
    print("-" * iCount)
        

def createRow(info:dict) -> dict:

    _symbol:str = str(info["symbol"])
    _low  = info["dayLow"]
    _high = info["dayHigh"]
    #_current =info["currentPrice"]
    _current =info["regularMarketPrice"]
    _diff    = round(_high - _low,2)
    _diff_per =  round((_diff * 100) / _low,2)

    objRet:dict = {}

    objRet["symbol"] = _symbol
    objRet["low"] = _low
    objRet["high"] = _high
    objRet["ltp"] = _current
    objRet["diff"] = _diff
    objRet["diff_per"] = _diff_per
    objRet["range52w"] = info["fiftyTwoWeekRange"]

    return objRet

def printRow(cols:list, r:dict):

    for _col in cols:

        #string padding
        sField :str = _col["field"]
        sVal :str = str(r[sField])
        sVal = getStrPaddding(_col,sVal)
        ###########

        #color Settings
        colorCode:str = "0"
        if "fcolor" in _col:
            sColorKey = _col["fcolor"]
            if sColorKey in foreColors:
                colorCode = foreColors[sColorKey]

        #color --Settings---

        if colorCode == "0":
            print(sVal,end="")
        else:
            print(f"\033[{colorCode}m{sVal}\033[0m",end="")
        
        print("|",end="")

    print("")

  
def printSymbolPrice(info:dict):
    _symbol:str = str(info["symbol"])
    _low  = info["dayLow"]
    _high = info["dayHigh"]
    _current =info["currentPrice"]
    _diff    = round(_high - _low,2)
    _diff_per =  round((_diff * 100) / _low,2)

    #printing cols
    print(f"{_symbol.ljust(15)}",end="|")
    print(f"{str(_current).rjust(8)}",end="|")
    print(f"\033[32m{str(_high).rjust(8)}\033[0m",end="|") 
    print(f"\033[31m{str(_low).rjust(8)}\033[0m",end="|")
    print(f"{str(_diff).rjust(8)}",end="|")
    print(f"{str(_diff_per).rjust(8)}",end="|")
    print("")
#----------

_grd = {}
_filePath:str = sys.argv[1]

with open("grid.json", 'r', encoding='utf-8') as file:
    _grd = json.load(file)

with open(_filePath, 'r', encoding='utf-8') as file:
    _grd["symbols"] = json.load(file)


_stocks = yf.Tickers(_grd["symbols"])
printHeader(_grd)

for sKey in _grd["symbols"]:
    stock = _stocks.tickers[sKey]
    r = createRow(stock.info)
    printRow(_grd["cols"],r)
