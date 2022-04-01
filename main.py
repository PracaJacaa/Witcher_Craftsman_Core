import PySimpleGUI as pg

names = []

f = open("names.txt","r")
for line in f:
    line=line.replace("\n","")
    names.append(line)

f.close()

pg.theme("darkAmber")
layout=[
    [pg.Text("enter name")],
    [pg.InputText()],
    [pg.Button("OK"), pg.Button("cancel")]

    ]
window = pg.Window("Witcher_Craftsman_Core", layout,margins=(500,300))
while True:
    event,values = window.read()
    if event == "cancel" or event ==pg.WIN_CLOSED:
        break
    print(values)
    print(names)


window.close()