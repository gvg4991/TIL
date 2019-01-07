blood_types={'A','B','A','O','AB','AB','O','A','B','O','B','AB'}

A=0
B=0
AB=0
O=0
for types in blood_types:
    if types == 'A':
        A+=1
    elif types == 'B':
        B+=1
    elif types == 'AB':
        AB+=1
    else:
        O+=1
print(f'A:{A}\nB:{B}\nAB:{AB}\nO:{O}')