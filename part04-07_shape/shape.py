# Copy here code of line function from previous exercise and use it in your solution
def line(number, string):
    if string == "":
        print (f"*" * number)
    else:
        print(string[0] * number)

def shape(width,char,height,filler):
    i = 0
    while i < width:
        i += 1
        line(i, char)
    i = 0
    while i < height:
        i += 1 
        line(width,filler)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")