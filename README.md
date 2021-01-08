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
    -   Username and hostname display
-   Configuration set in separate config file

## Install

- Clone this repository
- Execute `install.sh` giving the path to the directory you want to install the scripts in:
```
./install.sh /path/to/install/directory
```
- Place this line at the bottom of your `.bashrc` file, replacing `path/to/` with the path you gave to `install.sh`:
```
PROMPT_COMMAND=". path/to/prompt.sh"
```

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
-   `segementLength` : Size of the segment name. Can be used to avoid long directory names in the prompt. Set to 0 if you want no limit.
-   `showUsername` : If true, the first segment contains the username 
-   `showHostname` : If true, the first segment contains the hostname along with the username. If `showUsername` is not set, this option is inactive. 
-   `usernameDelimiter` : The character used to separate the username and the hostname. Only active if both `showUsername` and `showHostname` are set.

**For color gradient arrays:**
All colors must be hexadecimal color codes. You can put as many colors as you want in the arrays. If the path is longer than the number of colors in the arrays, it will loop back to the first color.

## Disable / Uninstall

- Remove the following line from your `.bashrc` file to disable the custom prompt
```
PROMPT_COMMAND=". path/to/prompt.sh"
```

- To uninstall completely the prompt, do the last step and delete the whole directory `shell-prompt` which is in the directory you gave to the install script

## Licence

Licensed under the MIT License.

**Created by const39.**
