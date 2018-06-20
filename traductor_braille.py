# import the library
from appJar import gui
import sys
import io
import braille as b

# handle button events
def press(button):
	ipt = app.getEntry("Entrada:")
	if button == "Grado 1":
		try:
			app.clearTextArea("Salida:")
			out = "{0}".format(b.traducir(ipt))
			print(out)
			app.setTextArea("Salida:",out)
		except LookupError:
			print("Error: use el formato correcto")
	elif button == "Grado 2":
		try:
			app.clearTextArea("Salida:")
			out = "{0}".format(b.reemplazargrado2(" " + ipt.lower() + " "))
			app.setTextArea("Salida:",out)
		except LookupError:
			print("Error: use el formato correcto")

# create a GUI variable called app
app = gui("Traductor Braille", "800x600")
app.setBg("orange")
app.setFont(30)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Traductor Braille")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("Entrada:")
app.addTextArea("Salida:")

# link the buttons to the function called press
app.addButtons(["Grado 1", "Grado 2"], press)

app.setFocus("Entrada:")

# start the GUI
app.go()