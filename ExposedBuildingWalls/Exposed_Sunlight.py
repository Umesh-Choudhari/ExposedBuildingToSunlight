import math

# Function to find heighest Point from buildings
def maxPointOfBuilding(building):
    maxPoint = None
    maxX = float("-inf")
    for vertex in building:
        if vertex[0] >= maxX:
            maxX = vertex[0]
            maxPoint = vertex

    return maxPoint

# Function to Check is Building on left, right side of source
def checkBuildingIsOnLeft(maxPoint, sourcePoint):
    if maxPoint[0] > sourcePoint[0]:
        return "Right"
    elif maxPoint[0] < sourcePoint[0]:
        return "Left"
    else:
        return "Is on Line"

# Function to Check is Height of Building is greater then source point 
def isAbove(maxPoint, source):
    if maxPoint[1] < source[1]:
        return "Above"
    elif maxPoint[1] > source[1]:
        return "Below"
    else:
        return "OnLine"

# Function to get legth of line 
def getLength(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Function to find intersection between two lines
def findIntersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    if x2 != x1 and x4 != x3:
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)

        if m1 == m2:
            return None

        c1 = y1 - m1 * x1
        c2 = y3 - m2 * x3

        x = (c2 - c1) / (m1 - m2)
        y = m1 * x + c1

    elif x2 == x1 and x4 == x3:
        if x1 != x3:
            return None

        y_min = min(y1, y2, y3, y4)
        y_max = max(y1, y2, y3, y4)
        y = (y_min + y_max) / 2
        x = x1

    else:
        if x2 == x1:
            m2 = (y4 - y3) / (x4 - x3)
            c2 = y3 - m2 * x3
            x = x1
            y = m2 * x1 + c2
        else:
            m1 = (y2 - y1) / (x2 - x1)
            c1 = y1 - m1 * x1
            x = x3
            y = m1 * x3 + c1
    return x, y

# Function to check point is present on the vertical line or not
def onVerticalLine(line, point):
    if line[0][1] < line[1][1]:
        if line[0][1] < point[1] and line[1][1] > point[1]:
            return True
        return False
    else:
        if line[1][1] < point[1] and line[0][1] > point[1]:
            return True
        return False

# Function to check point is present on the horizontal line or not
def onHorizontalLine(line, point):
    if line[0][0] < line[1][0]:
        if line[0][0] < point[0] and line[1][0] > point[0]:
            return True
        return False
    else:
        if line[1][0] < point[0] and line[0][0] > point[0]:
            return True
        return False

# Function to calculate the length exposed wall on the right side of source point
def calculateLengthOfExposedWallOnRightSide(buildingOnRightSide):
    sum = 0
    count = 0
    for building in buildingOnRightSide:

        if isAbove(building[0], source) == "Above" and count == 0:
            length = getLength(building[1][0], building[1][1])
            width = getLength(building[1][1], building[1][2])
            sum += length + width
            count += 1

        elif isAbove(building[0], source) == "Below" and count == 0:
            length = getLength(building[1][0], building[1][1])
            width = 0
            sum += length + width
            count += 1

        elif isAbove(building[0], source) == "OnLine" and count == 0:
            length = getLength(building[1][0], building[1][1])
            width = 0
            sum += length + width
            count += 1

        elif isAbove(building[0], source) == "Above" and count == 1:
            previousBuildingIndex = buildingOnRightSide.index(building) - 1
            line1 = [source, buildingOnRightSide[previousBuildingIndex][1][3]]
            line2 = [building[1][0], building[1][1]]
            line3 = [building[1][0], building[1][3]]

            vertical = findIntersection(line1, line2)
            horizontal = findIntersection(line1, line3)

            if onVerticalLine(line2, vertical):
                length = abs(getLength(line2[0], vertical))
                width = getLength(building[1][1], building[1][2])
                sum += length + width
            else:
                if line2[1][1] > vertical[1]:
                    length = abs(getLength(line2[0], line2[1]))
                    width = getLength(building[1][1], building[1][2])
                    sum += length + width
                else:
                    if onHorizontalLine(line3, horizontal):
                        width = getLength(horizontal, line3[1])
                        sum += width

        elif isAbove(building[0], source) == "Below" and count == 1:
            previousBuildingIndex = buildingOnRightSide.index(building) - 1
            line1 = [source, buildingOnRightSide[previousBuildingIndex][1][0]]
            line2 = [building[1][0], building[1][1]]
            line3 = [building[1][0], building[1][3]]

            vertical = findIntersection(line1, line2)
            horizontal = findIntersection(line1, line3)

            if onVerticalLine(line2, vertical):
                length = abs(getLength(line2[0], vertical))
                width = 0
                sum += length + width
    return sum

# Function to calculate the length of exposed wall on the Left side of source point
def calculateLengthOfExposedWallOnLeftSide(buildingOnLeftSide):
    sum = 0
    count = 0
    for building in buildingOnLeftSide:

        if isAbove(building[0], source) == "Above" and count == 0:
            length = getLength(building[1][0], building[1][1])
            width = getLength(building[1][1], building[1][2])
            sum += length + width
            count += 1

        elif isAbove(building[0], source) == "Below" and count == 0:
            length = getLength(building[1][0], building[1][1])
            width = 0
            sum += length + width
            count += 1

        elif isAbove(building[0], source) == "OnLine" and count == 0:
            length = getLength(building[1][0], building[1][1])
            width = 0
            sum += length + width
            count += 1

        elif isAbove(building[0], source) == "Above" and count == 1:
            previousBuildingIndex = buildingOnLeftSide.index(building) - 1
            line1 = [source, buildingOnLeftSide[previousBuildingIndex][1][0]]
            line2 = [building[1][2], building[1][3]]
            line3 = [building[1][0], building[1][3]]

            vertical = findIntersection(line1, line2)
            horizontal = findIntersection(line1, line3)

            if onVerticalLine(line2, vertical):
                length = abs(getLength(line2[0], vertical))
                width = getLength(building[1][1], building[1][2])
                sum += length + width
            else:
                if line2[1][1] > vertical[1]:
                    length = abs(getLength(line2[0], line2[1]))
                    width = getLength(building[1][1], building[1][2])
                    sum += length + width
                else:
                    if onHorizontalLine(line3, horizontal):
                        width = getLength(horizontal, line3[0])
                        sum += width

        elif isAbove(building[0], source) == "Below" and count == 1:
            previousBuildingIndex = buildingOnLeftSide.index(building) - 1
            line1 = [source, buildingOnLeftSide[previousBuildingIndex][1][3]]
            line2 = [building[1][2], building[1][3]]
            line3 = [building[1][0], building[1][3]]

            vertical = findIntersection(line1, line2)
            horizontal = findIntersection(line1, line3)

            if onVerticalLine(line2, vertical):
                length = abs(getLength(line2[0], vertical))
                width = 0
                sum += length + width
    return sum

# Function to calculate the legnth of exposed wall
def calculateLengthOfExposedWall(Buildings, source):
    buildingOnLeftSide = []
    buildingOnRightSide = []
    buildingIsOnLine = []
    for building in Buildings:
        maxPoint = maxPointOfBuilding(building)
        if checkBuildingIsOnLeft(maxPoint, source) == "Left":
            buildingOnLeftSide.append([maxPoint, building])
            
        elif checkBuildingIsOnLeft(maxPoint, source) == "Right":
            buildingOnRightSide.append([maxPoint, building])
            buildingOnRightSide = buildingOnRightSide[::-1]
        else:
            buildingIsOnLine.append([maxPoint, building])

    return calculateLengthOfExposedWallOnRightSide(buildingOnRightSide) + calculateLengthOfExposedWallOnLeftSide(buildingOnLeftSide)


if __name__ == "__main__":
    Buildings = [[[4,0],[4,-5],[7,-5],[7,0]]]
    source = [1,1]
    sum = calculateLengthOfExposedWall(Buildings, source)
    print("Length of exposed for %s is :- %s" % (Buildings,sum))

    print()
    print("----------------------------------------------------------------------------------------------")
    print()
    
    Buildings =  [[[4,0],[4,-5],[7,-5],[7,0]], [[0.4,-2],[0.4,-5],[2.5,-5],[2.5,-2]]]
    source =[1,1]
    sum = calculateLengthOfExposedWall(Buildings, source)
    print("Length of exposed for %s is :- %s" % (Buildings,sum))

