# shell-prompt

![example](screenshots/screenshot.png)

Custom Linux shell prompt written in Python.

## Features

-   Display the current working directory
-   Customizable color gradients for text and background
-   Can use TrueColors or 256-Colors for older terminals
-   Other options :
    -   Wrap `/home/<user>` in `~`
    -   Customizable segment number for long paths
    -   Customizable segment name length

-   Configuration set in separate config file

### Upcoming features

-   Display username is prompt

## Install

**TODO**

## Configure

Customisation is done in a JSON file. By default, the script will look for a file called `settings.json` but you can specify it manually in the command arguments, like that:

```
python3 prompt.py /path/to/settings/file.json
```

### Available settings

-   `background` : Used as the background colors for each segment in the prompt.
-   `foreground` : Used as the text colors for each segment in the prompt.
-   `truecolor` : Sets the color encoding used by the program to indicate the terminal which color to print.
    -   `true` will set the TrueColors encoding, which uses 24 bits to code the color. This is the standard encoding used by modern terminals. It allows a wide range of colors but can be unsupported by old terminals.
    -   `false` will set the 256-Colors encoding, which uses 8 bits to code the color. It allows a narrower range of colors but is supported by nearly every terminal.
-   `wrapHome` : If true, wraps the user directory segment (`/home/<user>`) using a tilde (`~`)
-   `segmentNumber` : Number of segment in the prompt. Can be used to avoid a long prompt when you deep dive in directories. Set to 0 if you want no limit.
-   `segementLength` : Size of the segement name. Can be used to avoid long directory names in the prompt. Set to 0 if you want no limit.

**For color gradient arrays:**
All colors must be hexadecimal color codes. You can put as many colors as you want in the arrays. If the path is longer than the number of colors in the arrays, it will loop back to the first color.

## Disable / Uninstall

**TODO**

## Licence

Licensed under the MIT License.

**Created by const39.**
