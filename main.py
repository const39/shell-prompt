# import color as c
from color import computeColor, TrueColorsEnabled
from os import getcwd

def buildName(name, textColorHex, backColorHex, nextBackColorHex):
    
    delim = ""
    # wrappingGroup = "\\[{}{}\\]"    # PS1
    wrappingGroup = "{}{}"    # debug

    textColor = computeColor(textColorHex, False)
    backColor = computeColor(backColorHex, True)
    delimColor = computeColor(backColorHex, False)
    nextBackColor = computeColor(nextBackColorHex, True)
    colorOff = computeColor()

    dirColorStr = wrappingGroup.format(backColor, textColor)
    dirStr = "\u00A0" + name + "\u00A0"
    delimColorStr = wrappingGroup.format(nextBackColor, delimColor)
    resetColorStr = wrappingGroup.format(colorOff, colorOff)

    return dirColorStr + dirStr + delimColorStr + delim + resetColorStr

path = getcwd()
textColors = ["#FFFFFF"]
backColors = ["#b82929",  "b0004b", "97086a", "cf6e00",  "36e25c", "00b5b8","247ba5","48437a","#4c0031","#860136","#b82929"]
TrueColorsEnabled = True

splittedPath = path.split('/')
splittedPath.pop(0)

pathIndex, textColorIndex, backColorIndex = 0, 0, 0
finalPrompt = ""
while pathIndex < len(splittedPath):

    if pathIndex == len(splittedPath) - 1:
        nextBackColorHex = ""
    else:
        nextBackColorIndex = 0 if len(backColors) == backColorIndex + 1 else backColorIndex + 1 
        nextBackColorHex = backColors[nextBackColorIndex]

    finalPrompt += buildName(splittedPath[pathIndex], textColors[textColorIndex], backColors[backColorIndex], nextBackColorHex)

    if textColorIndex + 1 >= len(textColors):
        textColorIndex = -1

    if backColorIndex + 1 >= len(backColors):
        backColorIndex = -1

    pathIndex += 1
    textColorIndex += 1
    backColorIndex += 1

print(finalPrompt, end="")