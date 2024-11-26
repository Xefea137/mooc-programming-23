# Write your solution here
from datetime import datetime
def is_it_valid(pic: str):
    text = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    if len(pic) != 11:
        return False

    if pic[6] != '+' and pic[6] != "-" and pic[6] != "A":
        return False

    cc = (int(pic[:6] + pic[7:10])%31)
    if text[cc] != pic[10]:
        return False

    if pic[6] == '+':
        d = pic[0:4] + '18' + pic[4:6]
    elif pic[6] == '-':
        d = pic[0:4] + '19' + pic[4:6]
    elif pic[6] == 'A':
        d = pic[0:4] + '20' + pic[4:6]

    try:
        datetime.strptime(d, "%d%m%Y")
    except ValueError:
        return False

    return True

if __name__ == "__main__":
    print(is_it_valid("290200+1239"))
    '''print(is_it_valid("081142-720N"))   #Wrong control
    print(is_it_valid("081842-720N"))   #Date wrong
    print(is_it_valid("230827-906F1"))  #Length PI wrong'''