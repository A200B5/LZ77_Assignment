class Tag:
    def __init__(self, distance, length, next_char):
        self.distance = distance
        self.length = length
        self.next_char = next_char

    def getLength(self):
        return self.length

    def getDistance(self):
        return self.distance

    def __str__(self):
        return f"<{self.distance}, {self.length}, {self.next_char}>"

def toBinary(number):
    if number == 0:
        return "0"

    binary = ""

    while number > 0:
        binary = str(number % 2) + binary
        number //= 2

    return binary


def charToBinary(c):
    number = ord(c)
    binary = ""

    while number > 0:
        binary = str(number % 2) + binary
        number //= 2

    return binary



with open("input.txt", "r") as file:
    data = file.read().strip()
    
tags = []

maxDistanceBits = 0
maxLengthBits = 0

output = ""


# Same idea as your Java Comparator:
# 1. Length descending
# 2. Distance ascending
def sort_key(tag):
    return (-tag.getLength(), tag.getDistance())


i = 0

while i < len(data):

    temp = []
    in_ = True

    j = 0

    while j <= i:

        if data[i] == data[j] and i == j and in_:
            tags.append(Tag(0, 0, data[i]))
            break

        elif data[i] == data[j] and i != j:
            in_ = False

            t = data[i]

            start = i
            end = j

            i += 1
            j += 1

            while (i < len(data) and j < len(data) and data[i] == data[j]):
                t += data[i]
                i += 1
                j += 1

            if i < len(data):
                t += data[i]

                temp.append(Tag(start - end,len(t) - 1,data[i]))

            else:
                temp.append(Tag(start - end,len(t), None))

            i = start
            j = end

        j += 1

    if len(temp) > 0:

        temp.sort(key=sort_key)

        tags.append(temp[0])

        i += temp[0].getLength()

    i += 1


for t in tags:

    counter = 0
    temp = t.distance

    while temp > 0:
        counter += 1
        temp //= 2

    if counter > maxDistanceBits:
        maxDistanceBits = counter


for t in tags:

    counter = 0
    temp = t.length

    while temp > 0:
        counter += 1
        temp //= 2

    if counter > maxLengthBits:
        maxLengthBits = counter


for t in tags:

    if len(toBinary(t.distance)) < maxDistanceBits:

        for i in range(maxDistanceBits - len(toBinary(t.distance))):
            output += "0"

    output += toBinary(t.distance)

    if len(toBinary(t.length)) < maxLengthBits:

        for i in range(maxLengthBits - len(toBinary(t.length))):
            output += "0"

    output += toBinary(t.length)

    if len(charToBinary(t.next_char)) < 8:

        for i in range(8 - len(charToBinary(t.next_char))):
            output += "0"

    output += charToBinary(t.next_char)


with open("output.txt", "w") as writer:
    writer.write(output)
