abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
rotY = [0]
Text = ['Text is: ']
def print_All(text):
    for i in range(1,25):
        print("----", i, "---------")
        print(rotX(i, text))

def rotX(Rot, text):
    if Rot == 0:
        print_All(text)

    Check = 0
    Text.clear()
    rotY.clear()
    new = list(text)
    rotY.append(Rot)
    for i in range(1, 27):

        if i + Rot > 25 and i + Rot < 52:
            x = i + Rot - 26
        elif i + Rot < 52:
            x = i + Rot
        else:
            raise ("The rot number must be between 0 and 25")
        rotY.append(x)

    for i in range(0, len(new)):

        for o in range(0, 26):
            if new[i] == abc[o]:
                Text.append(abc[rotY[o]])
                Check = i
            elif new[i] == ABC[o]:
                Text.append(ABC[rotY[o]])
                Check = i
        if Check != i:
            Text.append(new[i])
            o -= 1
        i -= 1
    end = ''.join(Text)
    return end
