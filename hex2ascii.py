## Hex  translate to Ascii
## 2019 12 19

def decode(hex_str):
    txt = hex_str
    txt_mid = ""
    m=7
    flag =m
    num=0

    while m>0:
        for i in txt:
            i = int(i)
            # print i
            num = num + i * (2 ** flag)
            flag = flag - 1
            if flag < 0:
                flag = m
                # print num
                txt_mid = txt_mid + chr(num)
                num = 0
                continue

        print (txt_mid)
        txt_mid = ""
        print("\n")
        m=m-1


if __name__ == "__main__":
    hex_str = "101010011010001101001111001101000001110100110010111110001110100010000011010011110011010000001101110101101110001011010011110100010000011001011101110110001111011111100100110010111001000100000110000111100111100011110100111010010101110010000010110011101111111010111100100100000111000011000011110011111001111101111101111111001011001000100000110100111100110100000110010111000011110011111100111100111110100110000111100101110100110010111100100101110"
    decode(hex_str)