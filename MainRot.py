abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's','t','u','v','w','x','y','z']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S','T','U','V','W','X','Y','Z']
rot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
rotY = [0]
Text = ['Text is: ']
def rotX(Rot, text):
    Check = 0
    Text.clear()
    new = list(text)
    rotY[0] = Rot
    for i in range(1, 26):

        if i + Rot > 25 and i + Rot < 52:
            x = i + Rot - 26
        elif i + Rot < 52:
            x = i + Rot
        else:
            raise ("The rot number must be between 0 and 25")
        rotY.append(x)

    for i in range(0, len(new)):

        for o in range(0, 23):
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
