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

f.close()