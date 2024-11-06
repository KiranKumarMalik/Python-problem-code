S=str(input("Enter a string: "))   # S="Hello"
dup={}                             # FIRST ITERATION       SECOND ITERATION     THIRD ITERATION            FORTH ITERATION          FIFTH ITERATION
for ch in S:                       # "H" in S              "e" in S             "l" in S                   "l" in S                 "o" in S
    if ch not in dup:              # if "H" not in dup     if "e" not in dup    if "l" not in dup          if "l" not in dup FALSE  if "o" not in dup
        dup[ch]=0                  # dup["H"]=0            dup["e"]=0           dup["l"]=0                                          dup["o"]=0
    else:                          # 
        dup[ch]=dup[ch]+1          #                                                                       dup["l"]=0+1
res=[]                             # dup={"H":0}           dup={"H":0,"e":0}    dup={"H":0,"e":0,"l":0}    dup={"H":0,"e":0,"l":1}  dup={"H":0,"e":0,"l":1,"o":0}
for keys,vals in dup.items():      #                                                                                                ([('H', 0), ('e', 0), ('l', 1), ('o',0)])
    if vals>0:                     #                                                                                                if vals>0:
        res.append(keys)           #                                                                                                ['l']
print(f"Duplicate characters are {res}")