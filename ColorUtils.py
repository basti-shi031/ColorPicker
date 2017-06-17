from PIL import Image


# 打开图片
def openImage(fileName):
    img = Image.open(fileName)
    return img


# 取前k个颜色
def classifyPixel(img, k):
    rgb_img = img.convert('RGB')
    width = img.size[0]
    height = img.size[1]
    colorDict = {}
    for w in range(width):
        for h in range(height):
            r, g, b = rgb_img.getpixel((w, h))
            key = str(r) + ',' + str(g) + ',' + str(b)
            colorDict[key] = colorDict.get(key, 0) + 1

    # 获得了以颜色为Key 像素点数量为value的dict
    sortColorDict = sorted(colorDict.items(), key=lambda d: d[1], reverse=True)
    sortedColorKList = []
    for index in range(k):
        sortedColorKList.append(sortColorDict[index])
    return sortedColorKList


# 转化为十六进制
def convert2Hex(sortColorKList):
    colorList = []
    for color in sortColorKList:
        colorStr = color[0]
        r, g, b = colorStr.split(',')
        hexR = hex(int(r))
        hexG = hex(int(g))
        hexB = hex(int(b))
        colorSymbol = standardizing(hexR, hexG, hexB)
        colorList.append(colorSymbol)
    return colorList


# 标准化
def standardizing(hexR, hexG, hexB):
    return '#' + str(hexR)[2:4].zfill(2) + str(hexG)[2:4].zfill(2) + str(hexB)[2:4].zfill(2)

# 获取颜色
def getColor(fileName):
    img = openImage(fileName)
    return convert2Hex(classifyPixel(img, 3))

