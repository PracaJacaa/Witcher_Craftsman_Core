import PySimpleGUI as pg
import Datasheet

###NO MORE DATA DOWN 

Data_head=["Name","Crafting dc","Time","Timber","Iron","Fethers","Hardened Leather","Steel","Investmend","Cost"]
pg.theme("darkAmber")
layout=[
    [pg.Text("enter name")],
    [pg.InputText()],
    [pg.Table(values=Datasheet.data,headings=Data_head,
                    auto_size_columns=True,
                    justification='right',
                    tooltip='This is a table')],
    [pg.Button("OK"), pg.Button("cancel")]

    ]
window = pg.Window("Witcher_Craftsman_Core", layout,margins=(500,300))
while True:
    event,values = window.read()
    if event == "cancel" or event ==pg.WIN_CLOSED:
        break


window.close()