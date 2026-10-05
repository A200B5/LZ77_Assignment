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


data = input()

tags = []

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


for tag in tags:
    print(tag)
