#Caesar Crypto  program
####2019/12/18

def caesar(txt):
    asc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    txt1=txt
    j=1
    txt2=""
    while j<=24:
        for i in txt1:
            if i in asc:
                num = asc.find(i)
                num = num - j
                if num <0:
                    num = num + len(asc)
                txt2 = txt2 + asc[num]
            else:
                txt2 = txt2 + " "
        j+=1
        print (txt2)
        print ("\n")
        txt2 = ""

if __name__ == '__main__':
    strs = "HVS EIWQY PFCKB TCL XIADG CJSF HVS ZONM RCU CT QOSGOF OBR MCIF IBWEIS GCZIHWCB WG BOBPQVAVBTDD"
    caesar(txt=strs)