#!/usr/bin/env python3

import sys
import io
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import braille as b

helpstr = "uso: {0} archivo_entrada archivo_salida".format(sys.argv[0])

if len(sys.argv) == 1:
	root = Tk()
	root.withdraw()
	fi = io.open(filedialog.askopenfilename(), "r", encoding='utf8')
	fo = io.open(filedialog.asksaveasfilename(), "w", encoding='utf8')
elif len(sys.argv) == 3:
	fi = io.open(sys.argv[1], "r", encoding='utf8')
	fo = io.open(sys.argv[2], "w", encoding='utf8')
else:
	print(helpstr)
	sys.exit(2)
try:
	fo.write(b.traducir(fi.read()))
finally:
	fi.close()
	fo.close()
