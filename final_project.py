#coding:gbk
"""
作者：徐佳梁
程序：实现对文本破晓黎明的街道.txt进行提取人物关系文件
基本思路：一般认为，在一篇文章中的同一段出现的两个人物之间，具有某种关联。以此进行统计人物关系。
"""
#导入库，jieba库
import jieba
import jieba.posseg as psg#词性标注模块
#jieba库用法，一些函数掌握。（需要导入加载字典dict.txt）
jieba.load_userdict('dict.txt')

#先建立好人物名字的词频字典类型，键为人物名字，值为：出现频率
#人物之间联系程度的字典，键为：两个人物的名字，值为同一行出现的次数。

name={}   #key:name,value:f
connection={}#key;人物,value:另一个人物，极其同行次数
NameLine=[]
#读取文件，对每一行进行读取。

with open('黎明破晓的街道.txt') as f:
    for line in f.readlines():
# 读取之后进行使用jieba库分词处理jieba.cut()，获得名字分词。
#Jieba有三种分词模式，jieba.cut(  , cut_all=True),jieba.cut(  ,cut_all=False),jieba.cut_for_search(),cut前加l输出列表，jeba.lcut（）
#第二种方法较好分词
        nameline=psg.cut(line)#标注词性
        NameLine.append([])

        for words in nameline:

          if words.flag != 'nr'  or len(words.word)<=1:
              continue
          NameLine[-1].append(words.word)
          if name.get(words.word) is None:
              name[words.word]=0
              connection[words.word] = {}
          name[words.word] += 1

with open('node.csv','w') as f:
    f.write("Id Label Weight\r\n")
    for names,freq in name.items():
        f.write(names+" "+names+" "+str(freq)+"\r\n")
#node点代表的是人物出现频率及权重（在软件中表示点的大小），edge代表的是某两个人物之间联系紧密与否（在软件中体现的是边连线的线宽）

#得到各人物词频
# print(NameLine)
# print(connection)
# for x in NameLine:
#     if len(x) ==1:
#         NameLine.remove(x)

for line in  NameLine:
    # print(line)
    for name1 in line:
        for name2 in line:
              if name1==name2:
                  continue
              if connection[name1].get(name2) is None:
                  connection[name1][name2]=1
              else:
                  connection[name1][name2] = connection[name1][name2] + 1
# print(connection)
for x in list(connection.keys()):
    if connection[x]=={}:
        del connection[x]
# print(connection)

with open("edge.csv", "w") as f:
    f.write("Source Target Weight\r\n")

    for name, edges in connection.items():

        for v, w in edges.items():

            if w > 3:
                f.write(name + " " + v + " " + str(w) + "\r\n")
#edge:两个人物关系程度
#以文本进行输出（.csv文件）
#建立人物联系