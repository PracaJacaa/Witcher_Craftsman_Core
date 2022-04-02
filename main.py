import PySimpleGUI as pg
import Datasheet

###NO MORE DATA DOWN 

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
    print(Datasheet.Name) #debug


window.close()