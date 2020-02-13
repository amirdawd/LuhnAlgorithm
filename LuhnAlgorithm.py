file_object = open('Cards.txt', 'r')
cardVector = []
for x in file_object:
    cardVector.append(x)

constVector = []

for x in range(0,16):
    if x%2==0:
        constVector.append('2')
    else:
     constVector.append('1')

def replace_x(card):
    temp_vector = []
    index = 0
    count = 0
    for c in card:
        if c == 'X':
            index = count
            c = c.replace('X', '0')
        temp_vector.append(c.strip())
        count = count + 1
    temp_vector = ' '.join(temp_vector).split()
    return temp_vector, index


def sum_card(card):
    sumCard = 0
    index = 0
    for x in card:
        temp = 0
        x = int(x)
        y = int(constVector[index])
        temp = x * y
        if temp > 9:
            temp = temp - 9
        sumCard = sumCard + temp
        index = index + 1
    return sumCard


def find_x(card):
    card, index = replace_x(card)
    tempX = 10 - (sum_card(card) % 10)
    c = int(constVector[index])
    if c % 2 == 0:
        if tempX % 2 == 0:
            x= (tempX+9)
            if tempX % 2 == 0:
                x= tempX/2
            else:
                x/=2
    if tempX==10:
        tempX=0
    return int(tempX)


def main ():
    cardlist = cardVector
    print(cardlist)
    test_file = open('L.txt', 'w')
    for x in cardlist:
        print(str(find_x(x)))
        test_file.write(str(find_x(x)))


if __name__ == "__main__":
    main()
