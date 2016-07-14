import ctypes
lib = ctypes.cdll.LoadLibrary('../DllExample/bin/x86/Debug/DllExample.dll')

import time

# 0.04s
start = time.clock()
x = lib.add(3, 5)
print("{:.6f}".format(time.clock()-start))

# 0.000006s
start = time.clock()
x = 3+5
print("{:.6f}".format(time.clock()-start))