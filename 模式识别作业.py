import csv
import random
import math
import operator
#获取数据，并分割数据为训练集和测试集
# def loaddatas(filename, a, train, tests ):
train = []
tests = []
a = float(5/12)
with open('irisdata.txt', 'rt') as file:
    lines = csv.reader(file)
    datas = list(lines)
    # print(len(datas))测试
    for x in range(len(datas)-1):
        for y in range(4):
            datas[x][y] = float(datas[x][y])
        if random.random() < a:
            train.append(datas[x])
        else:
            tests.append(datas[x])
#print(tests,train)
def get_distance(neighbors1, neighbors2, leng):
    distance = 0
    #计算所有维度的差的平方和，此处传入的leng其实就是数据的维度
    #举例[3,4,5,8]的维度就是4
    for x in range(leng):
        distance += math.pow((neighbors1[x]-neighbors2[x]), 2)
    return math.sqrt(distance)
pre_results = []
k = 7
for x in range(len(tests)):
    # traintrain[x]
    #获取某个待分类数据的k个邻居
    distances = []
    leng = len(tests[x]) - 1  # 测试集的维度
    for y in range(len(train)):  # 对训练集中的每一个数据计算它到测试元的距离
        # testone
        dist = get_distance(tests[x], train[y], leng)
        distances.append((train[y], dist))
        # distances.append(dist)
    distances.sort(key=operator.itemgetter(1))  # 对距离从小到大进行排序
    neighbors_t= []
    for x in range(k):
        neighbors_t.append(distances[x][0])
    # print(neighbors)
    #根据求得的邻居获取他们的属性并进行投票
    classVotes = {}
    for x in range(len(neighbors_t)):
        response = neighbors_t[x][-1]  # 提取邻居的属性
        if response in classVotes:  # 对k个邻居进行属性投票
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    # print(classVotes)
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)  # 邻居的属性从大到小进行排序
    # print(sortedVotes)
    result = sortedVotes[0][0]
    pre_results.append(result)
    # print ('>predicted=' + repr(result) + ', actual=' + repr(tests[x][-1]))
#显示预测正确率
correct = 0
for x in range(len(tests)):
    if tests[x][-1] == pre_results[x]:
        correct += 1
print('预测正确率',(correct/float(len(tests)))*100.0)



