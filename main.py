import tkinter as tk
from tkinter import messagebox
from configparser import ConfigParser
import os

# Import the TextEditor class from your `editor.py` module
from editor import TextEditor

def load_config():
    config = ConfigParser()
    config_file_path = os.path.expanduser("~/.config/mcfg")
    
    # Check for Windows and use appropriate path if needed
    if os.name == 'nt':
        config_file_path = os.path.join(os.environ['USERPROFILE'], 'mcfg')

    # If config file doesn't exist, create one with default values
    if not os.path.exists(config_file_path):
        with open(config_file_path, 'w') as configfile:
            config['DEFAULT'] = {
                'first': '1',
                'color': '#000000',  # Default color set to black in hex
                'font': 'Arial',
                'size': '10',
                'tspvalue': '0.5'
            }
            config.write(configfile)
    else:
        config.read(config_file_path)

    return config

def is_valid_hex_color(color):
    """Check if a string is a valid hex color code."""
    if color.startswith("#") and len(color) == 7:
        try:
            int(color[1:], 16)
            return True
        except ValueError:
            return False
    return False

def apply_config(root, text_editor, config):
    bg_color = config['DEFAULT'].get('color', '#FFFFFF')  # Default to white if not set
    if not is_valid_hex_color(bg_color):
        bg_color = 'white'  # Fallback to a named color if the hex is invalid
    
    font_name = config['DEFAULT'].get('font', 'Arial')
    font_size = config['DEFAULT'].getint('size', 10)
    transparency = config['DEFAULT'].getfloat('tspvalue', 0.5)
    
    # Set text widget background color
    text_editor.text.config(bg=bg_color)
    # Set text widget font
    text_editor.text.config(font=(font_name, font_size))
    # Apply transparency to the main window
    root.attributes('-alpha', transparency)

def main():
    root = tk.Tk()
    config = load_config()
    text_editor = TextEditor(root, config)
    apply_config(root, text_editor, config)
    root.mainloop()

if __name__ == "__main__":
    main()
