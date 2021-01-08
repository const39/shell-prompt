from color import computeColor, TrueColorsEnabled
from os import getcwd, getenv
from sys import argv
import json

def parseSettings():
    """
    Parse the JSON settings file and return settings as a dictionary.
    """
    # Default filename
    filename = "settings.json"
    # If a settings file in given, use it
    if len(argv) > 1:
        filename = argv[1]
    # Open the file
    file = open(filename, 'r')
    # Return the parsed JSON as a dictionary or exit with error code if the file was not valid JSON 
    try:
        return json.load(file)
    except json.JSONDecodeError:
        print(filename, "is not a valid settings file in JSON format.")
        exit(1)

def buildName(name, textColorHex, backColorHex, delimBackColorHex):
    """
    Build a string segment terminated by a delimiter.
    
    Parameters:
        name (string): the segment text, usually the directory name 
        textColorHex (string): hexadecimal color code used for the text
        backColorHex (string): hexadecimal color code used as the text background
        delimBackColorHex (string): hexadecimal color code used as the delimiter background

    Returns:
        The string formatted with color codes.
    """
    delim = "" # Delimiter
    # wrappingGroup = "\\[{}{}\\]"    # ! final
    wrappingGroup = "{}{}"    # debug

    # Generate color codes
    textColor = computeColor(textColorHex, False)
    backColor = computeColor(backColorHex, True)
    delimColor = computeColor(backColorHex, False)
    delimBackColor = computeColor(delimBackColorHex, True)
    colorOff = computeColor()

    # Format groups with color codes
    dirColorStr = wrappingGroup.format(backColor, textColor)
    dirStr = "\u00A0" + name + "\u00A0"
    delimColorStr = wrappingGroup.format(delimBackColor, delimColor)
    resetColorStr = wrappingGroup.format(colorOff, colorOff)

    # Put groups together
    return dirColorStr + dirStr + delimColorStr + delim + resetColorStr

# *** Main script *** #

path = getcwd() # Get current working directory
settings = parseSettings()  # Get settings from file

TrueColorsEnabled = settings['truecolor']   # Set color encoding according to settings

# Wrap home dir with '~' if the option is set
if settings['wrapHome']:
    homeDir = getenv('HOME')    # Get Home dir from OS
    path = path.replace(homeDir, '~', 1)    # Replace '/home/<user>' with '~'

elif path[0] == '/':
    path = path[1:]  # Remove first '/' to avoid empty element in list

splittedPath = path.split('/')  # Split path in list

# Init indices and prompt
pathIndex, textColorIndex, backColorIndex = 0, 0, 0
finalPrompt = ""

# Build a segment for each directory 
while pathIndex < len(splittedPath):

    # If it's the last element of the path, no background color for the delimiter
    if pathIndex == len(splittedPath) - 1:
        delimBackColorHex = ""
    # Else, get the next background color index for the delimiter background color
    else:
        # If we've reached the end of the background colors list, loop back to the start
        if len(settings['background']) == backColorIndex + 1:
            index = 0 
        # Otherwise, use the next color in the list
        else:
            index = backColorIndex + 1 
        delimBackColorHex = settings['background'][index]

    # Append the new segment to the prompt
    finalPrompt += buildName(name=splittedPath[pathIndex],
                             textColorHex=settings['foreground'][textColorIndex],
                             backColorHex=settings['background'][backColorIndex],
                             delimBackColorHex=delimBackColorHex)

    # If we've reached the end of the foreground colors list, loop back to the start
    if textColorIndex + 1 >= len(settings['foreground']):
        textColorIndex = -1

    # If we've reached the end of the background colors list, loop back to the start
    if backColorIndex + 1 >= len(settings['background']):
        backColorIndex = -1

    # Increment indices
    pathIndex += 1
    textColorIndex += 1
    backColorIndex += 1

# Print the whole prompt
# print(finalPrompt, end="")  # ! final
print(finalPrompt)  # debug
