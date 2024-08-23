# meow
A cross-platform simple text/code editor written on Python and tkinter

## Backstory
I was ricing FreeBSD one day while noticing that I'm missing a text editor. I can't put VS Code on a virtual machine with 1.5GB RAM, and I can't use Vim/Neovim. I intended to fork [nano](https://nano-editor.org/) to add some more colors and features but I don't understand C. So I wrote this in one night and the next morning to fit the BSD system.

## Etymology
`cat` is an Unix command which creates a new text file and allows us to edit them right after that. I named this project after a cat's crying sound, which is, meow. Before then. the project is named py-meow.

## Features
### Available now
- No menu bar, hotkey only
- Notepad-style formatting
- A character counter
- Config file
- Transparency
- Save/save as/load/create new
- Background color
- Find

### Missing/to be added
- per-line counter (I can't get this to work)
- syntax highlighting
- underscore and other text highlighting. I won't add these to keep the program simple
- replace (top priority)
- keyboardless selecting. My intention is to hold Alt and use arrow keys to move the cursor to select.
- colored text (in general)
- many more

## Advantages over nano
- Easier-to-read code with description
- Color support
- GUI
- No cheatsheet
- Native file browser support
- Runs pretty much everywhere without modification

## Installation and configuration
- Clone this respiratory
- Run main.py. If it's your first time running, it'll generate a config file
### Configuration
The config file resides in your home direction regardless of OS. It's 'C:/Users/your_username' on Windows and ~/.config/ on most Linux distros, Unix and BSD OS. The file's name is "mcfg". Open it with a text editor (like this one).
TBA

## User's guide
TBA

## Help/support me
- Read and review the code
- File a bug complaint
- Commit changes
- Improve features

## Thanks
- ChatGPT
- me
