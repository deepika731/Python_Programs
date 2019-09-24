def timeConversion(s):
    #
    # Write your code here.
    #
    print(s[8:10])
    if(s[9:11] == "AM"):
        if(s[0:2] == "12"):
            s.replace(s[0:2], "00")
    else:
        print(int(s[0:2]))
        s = s.replace(s[0:2], str(int(s[0:2]) + 12))
        print(s)
    return s

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)
