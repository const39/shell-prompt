# Sets the color encoding which will be used:
#   - True : use Truecolors (24 bits encoding) - default
#   - False: use 256-colors (8 bits encoding)
TrueColorsEnabled = True

def _asTruecolorString(rgb):
    """
    Encode the given color as a Truecolor string

    Parameters:
        rgb (tuple): a tuple containing Red, Green and Blue information

    Returns:
        The encoded string
    """
    return "2;{};{};{}".format(rgb[0], rgb[1], rgb[2]) 

def _as256String(rgb):
    """
    Encode the given color as a 256-colors string

    Parameters:
        rgb (tuple): a tuple containing Red, Green and Blue information

    Returns:
        The encoded string
    """
    redRatio = (0 if rgb[0] < 75 else (rgb[0] - 35) / 40) * 6 * 6
    greenRatio = (0 if rgb[1] < 75 else (rgb[1] - 35) / 40) * 6 
    blueRatio = (0 if rgb[2] < 75 else (rgb[2] - 35) / 40) + 16
    return "5;{}".format(int(redRatio + greenRatio + blueRatio))

def _extractRGBFromHex(hexCode):
    """
    Extract RGB information from an hexadecimal color code

    Parameters:
        hexCode (string): an hexadecimal color code

    Returns:
        A tuple containing Red, Green and Blue information
    """
    hexCode = hexCode.lstrip('#')   # Remove the '#' from the string

    # Convert each byte into decimal, store it in a tuple and return 
    return tuple(int(hexCode[i:i+2], 16) for i in (0, 2, 4))

def computeColor(hexCode = "", isBackground = False):
    """
    Encode a color from its hex code as the currently selected encoding (@see TrueColorsEnabled).
    If the color is transparent, set 'hexCode' to an empty string.

    Parameters:
        hexCode (string): the color hexadecimal code
        isBackground (bool): indicated if the color is used as background or foreground

    Returns:
        A color encoded as a string
    """
    # If no hex code, return no color/transparent color code. 
    if hexCode == "":
        return "\033[0m"
    
    # Extract RGB info from hex code
    rgb = _extractRGBFromHex(hexCode)

    # Encode color according to current setting
    if TrueColorsEnabled:
        color = _asTruecolorString(rgb)
    else:
        color = _as256String(rgb)
    
    # Add encoding prefix according to isBackground bool
    if isBackground:
        prefix = "\033[48;" 
    else:
        prefix = "\033[38;" 
    
    return "{}{}m".format(prefix, color)
