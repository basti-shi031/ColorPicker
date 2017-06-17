import ColorUtils

# 生成
def createResource(fileName, colorList):
    f = open(fileName, encoding='utf-8')
    resource = ''
    for line in f.readlines():
        resource = line
    resourceList = []
    for index in range(len(colorList)):
        formatResource= resource % ('color' + str(index), colorList[index])
        resourceList.append(formatResource)
    return resourceList


print(createResource("android_resource", ColorUtils.getColor('bd.png')))
