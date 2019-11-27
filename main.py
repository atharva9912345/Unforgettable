#main file
import sys

sys.path.insert(0, 'res')
sys.path.insert(0, 'bin')

import func

print("Application started.")


if(not func.checkFileExists("bin/gp.txt")):
    import signup
    signup.showWindow()
else:
    import mainscr
    mainscr.showWindow()
