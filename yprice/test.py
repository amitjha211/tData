import os
import json

# symbol:str = "DABUR.NS"
# lotsize:int = 1250
# currentPrice:float = 412.5

# lstPos = [
#     { "qty" : 0.00 ,"price" : 0.00 ,"amount" : 0.00 }
# ]
# print(currentPrice * lotsize)

_root_path:str=os.getenv("AJ_APK_PATH")
_file_path:str=f"{_root_path}/qbt/cli/grid.json"
print(_file_path)

with open(_file_path, 'r', encoding='utf-8') as file:
    _grd = json.load(file)
    print(_grd)
