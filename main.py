import PySimpleGUI as pg
import csv
f=open("dane.csv","r")
file = csv.DictReader(f)

Name=[]
CraftingDc=[]
Time=[]
Timber=[]
Iron=[]
Fethers=[]
Hardened_Leather=[]
Steel=[]
Investmend=[]
Cost =[]

for col in file:
    Name.append(col["Name"])
    CraftingDc.append(col["Crafting dc"])
    Time.append(col["Timber"])
    Fethers.append(col["Fethers"])
    Hardened_Leather.append(col["Hardened Leather"])
    Steel.append(col["Steel"])
    Investmend.append(col["Investmend"])
    Cost.append(col["Cost"])


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
    print(Name)


window.close()