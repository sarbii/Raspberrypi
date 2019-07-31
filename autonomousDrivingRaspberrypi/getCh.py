def getch():
    import sys, tty, termios
    old_settings = termios.tcgetattr(0)
    new_settings = old_settings[:]
    new_settings[3] &= ~termios.ICANON
    try :
	    termios.tcsetattr(0, termios.TCSANOW, new_settings)
	    ch = sys.stdin.read(1)
    finally:
	    termios.tcsetattr(0, termios.TCSANOW, old_settings)
    return ch
