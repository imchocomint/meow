import os
import tkinter as tk
from tkinter import filedialog, messagebox, font
import configparser
from editor import TextEditor

def get_config_path():
    if os.name == 'nt':  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'mcfg')
    else:  # Linux
        return os.path.join(os.path.expanduser('~'), '.config', 'mcfg')

def load_config():
    config_path = get_config_path()
    config = configparser.ConfigParser()

    if not os.path.exists(config_path):
        config['DEFAULT'] = {
            'first': '1',
            'color': '#000000',
            'font': 'Arial',
            'size': '14',
            'tspvalue': '0.5'
        }
        with open(config_path, 'w') as configfile:
            config.write(configfile)
    else:
        config.read(config_path)
    
    return config


if __name__ == "__main__":
    root = tk.Tk()
    config = load_config()

    # Apply appearance settings from config
    #print(f"Background color from config: {config['DEFAULT']['color']}")
    #root.config(bg=config['DEFAULT']['color'])
    #root.config(bg='#ff0000')
    root.attributes('-alpha', float(config['DEFAULT']['tspvalue']))
    
    editor = TextEditor(root, config)
    root.mainloop()
