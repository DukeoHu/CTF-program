##url decode  program
##2019 12 19

def main(ox_strs):
    flag = 0
    url_txt = ox_strs
    decode_txt =""
    txt1=url_txt.split("%")
    txt1=txt1[1:]
    print (txt1)
    str_num = "0123456789ABCDEF"
    for i in txt1:
        for j in i:
            num = str_num.find(j)
            if flag ==0:
                num1 = num * 16
            flag = 1
        num = num + num1
        decode_txt = decode_txt + chr(num)
        flag = 0
    print (decode_txt)

if __name__ == "__main__":
    ox_str = "%59%69%70%70%65%68%21%20%59%6F%75%72%20%55%52%4C%20%69%73%20%63%68%61%6C%6C%65%6E%67%65%2F%74%72%61%69%6E%69%6E%67%2F%65%6E%63%6F%64%69%6E%67%73%2F%75%72%6C%2F%73%61%77%5F%6C%6F%74%69%6F%6E%2E%70%68%70%3F%70%3D%61%65%72%65%61%65%67%73%70%66%68%73%26%63%69%64%3D%35%32%23%70%61%73%73%77%6F%72%64%3D%66%69%62%72%65%5F%6F%70%74%69%63%73%20%56%65%72%79%20%77%65%6C%6C%20%64%6F%6E%65%21"
    ox_str2 = "%E5%AF%86%E7%A0%81"
    main(ox_str2)