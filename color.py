TrueColorsEnabled = True

def _asTruecolorString(rgb):
    return "2;{};{};{}".format(rgb[0], rgb[1], rgb[2]) 

def _as256String(rgb):
    redRatio = (0 if rgb[0] < 75 else (rgb[0] - 35) / 40) * 6 * 6
    greenRatio = (0 if rgb[1] < 75 else (rgb[1] - 35) / 40) * 6
    blueRatio = (0 if rgb[2] < 75 else (rgb[2] - 35) / 40) + 16
    return "5;{}".format(int(redRatio + greenRatio + blueRatio))

def _extractRGBFromHex(hexCode):
    hexCode = hexCode.lstrip('#')
    return tuple(int(hexCode[i:i+2], 16) for i in (0, 2, 4))

def computeColor(hexCode = "", isBackground = False):
    if hexCode == "":
        return "\033[0m"
    
    rgb = _extractRGBFromHex(hexCode)
    if TrueColorsEnabled:
        color = _asTruecolorString(rgb)
    else:
        color = _as256String(rgb)
    
    if isBackground:
        prefix = "\033[48;" 
    else:
        prefix = "\033[38;" 
    
    return "{}{}m".format(prefix, color)