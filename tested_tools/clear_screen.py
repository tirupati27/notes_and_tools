import os

def clear_screen():
    """
    It clear the terminal in platform independent way
    """
    os.system("cls" if os.name == "nt" else "clear")