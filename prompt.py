#!/bin/env python3
from color import computeColor, TrueColorsEnabled
from os import getcwd, getenv
from os.path import dirname, realpath
from sys import argv
from getpass import getuser
from socket import gethostname
import json

def parseSettings():
    """
    Parse the JSON settings file and return settings as a dictionary.
    """
    # Search for default file in same directory as script
    filename = dirname(realpath(__file__)) + "/settings.json"
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

def buildName(name, delimiter, textColorHex, backColorHex, delimBackColorHex):
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
    wrappingGroup = "\\[{}{}\\]"

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
    return dirColorStr + dirStr + delimColorStr + delimiter + resetColorStr

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

# Limit the number of segments to the given value
if settings['segmentNumber'] > 0 and settings['segmentNumber'] < len(splittedPath):
    i = len(splittedPath) - settings['segmentNumber']
    splittedPath = splittedPath[i:]

# Limit the length of each segement to the given value
if settings['segmentLength'] > 0:
    truncatedNames = [] # Create new list to store truncated names
    for elem in splittedPath:
        # If the name is longer than wanted, truncate it
        if len(elem) > settings['segmentLength']:
            truncatedNames.append(elem[0:settings['segmentLength']])
        # If the name is already small enough, just add it to the new list
        else:
            truncatedNames.append(elem)
    splittedPath = truncatedNames

# Show username in prompt if option set
if settings['showUsername']:

    # Show hostname along username if option set
    if settings['showHostname'] and settings['usernameDelimiter']:
        txt = "{} {} {}".format(getuser(), settings['usernameDelimiter'], gethostname())
    # Otherwise show only username
    else:
        txt = getuser()
    # Insert new segement in list
    splittedPath.insert(0, txt)

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

    # For first segment if it's the username, empty delimiter
    if settings['showUsername'] and pathIndex == 0:
        delim = ""
    # For other segments, set other delimiter
    else:
        delim = ""

    # Append the new segment to the prompt
    finalPrompt += buildName(name=splittedPath[pathIndex],
                             delimiter=delim,
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
print(finalPrompt, end="")