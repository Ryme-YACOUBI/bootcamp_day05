def Scrabbles(ch):
    s=0
    for i in range(0,len(ch)):
        if ch[i] in "AEIOULNSTR":
            s=s+1
        elif ch[i] in "DG":
            s=s+2
        elif ch[i] in "BCMP":
            s=s+3
        elif ch[i] in "FHVWY":
            s=s+4
        elif ch[i] in "K":
            s=s+5
        elif ch[i] in "JX":
            s=s+8
        elif ch[i] in "QZ":
            s=s+10
    return s
        