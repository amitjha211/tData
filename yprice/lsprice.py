import json
import sys
import yfinance as yf
import cliGrid
import os

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
  
# def printSymbolPrice(info:dict):
#     _symbol:str = str(info["symbol"])
#     _low  = info["dayLow"]
#     _high = info["dayHigh"]
#     _current =info["currentPrice"]
#     _diff    = round(_high - _low,2)
#     _diff_per =  round((_diff * 100) / _low,2)

#     #printing cols
#     print(f"{_symbol.ljust(15)}",end="|")
#     print(f"{str(_current).rjust(8)}",end="|")
#     print(f"\033[32m{str(_high).rjust(8)}\033[0m",end="|") 
#     print(f"\033[31m{str(_low).rjust(8)}\033[0m",end="|")
#     print(f"{str(_diff).rjust(8)}",end="|")
#     print(f"{str(_diff_per).rjust(8)}",end="|")
#     print("")
#----------

_grd = {}

_root_path:str=os.getenv("AJ_APK_PATH")
_grid_path:str=f"{_root_path}/qbt/cli/grid.json"

with open(_grid_path, 'r', encoding='utf-8') as file:
    _grd = json.load(file)

_filePath:str = sys.argv[1]
with open(_filePath, 'r', encoding='utf-8') as file:
    _grd["symbols"] = json.load(file)


_stocks = yf.Tickers(_grd["symbols"])
cliGrid.printHeader(_grd)

for sKey in _grd["symbols"]:
    stock = _stocks.tickers[sKey]
    r = createRow(stock.info)
    cliGrid.printRow(_grd["cols"],r)
