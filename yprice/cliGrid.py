
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

