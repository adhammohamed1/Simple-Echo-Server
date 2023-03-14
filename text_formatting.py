
COLOR_RED = 1
COLOR_GREEN = 2
COLOR_YELLOW = 3
COLOR_BLUE = 4
COLOR_MAGENTA = 5
COLOR_CYAN = 6
COLOR_WHITE = 7
COLOR_BLACK = 8
COLOR_GREY = 9

def reset_formatting():
    return "\033[0m"

def set_bold():
    return "\033[1m"

def set_underline():
    return "033[4m"

def set_foreground_color(color):
    return "\033[38;5;" + str(color) + "m"

def set_background_color(color):
    return "\033[48;5;" + str(color) + "m"

def set_foreground_color_rgb(r, g, b):
    return "\033[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

def set_background_color_rgb(r, g, b):
    return "\033[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

