from color import computeColor, TrueColorsEnabled
from os import getcwd
from sys import argv
import json

def parseSettings():
    filename = "settings.json"
    if len(argv) > 1:
        filename = argv[1]
    file = open(filename, 'r')
    try:
        return json.load(file)
    except json.JSONDecodeError:
        print(filename, "is not a valid settings file in JSON format.")
        exit(1)

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
settings = parseSettings()

TrueColorsEnabled = settings['truecolor']

splittedPath = path.split('/')
splittedPath.pop(0)

pathIndex, textColorIndex, backColorIndex = 0, 0, 0
finalPrompt = ""
while pathIndex < len(splittedPath):

    if pathIndex == len(splittedPath) - 1:
        nextBackColorHex = ""
    else:
        nextBackColorIndex = 0 if len(settings['background']) == backColorIndex + 1 else backColorIndex + 1 
        nextBackColorHex = settings['background'][nextBackColorIndex]

    finalPrompt += buildName(splittedPath[pathIndex], settings['foreground'][textColorIndex], settings['background'][backColorIndex], nextBackColorHex)

    if textColorIndex + 1 >= len(settings['foreground']):
        textColorIndex = -1

    if backColorIndex + 1 >= len(settings['background']):
        backColorIndex = -1

    pathIndex += 1
    textColorIndex += 1
    backColorIndex += 1

print(finalPrompt, end="")
