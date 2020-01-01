#coding:gbk
"""
���ߣ������
����ʵ�ֶ��ı����������Ľֵ�.txt������ȡ�����ϵ�ļ�
����˼·��һ����Ϊ����һƪ�����е�ͬһ�γ��ֵ���������֮�䣬����ĳ�ֹ������Դ˽���ͳ�������ϵ��
"""
#����⣬jieba��
import jieba
import jieba.posseg as psg#���Ա�עģ��
#jieba���÷���һЩ�������ա�����Ҫ��������ֵ�dict.txt��
jieba.load_userdict('dict.txt')

#�Ƚ������������ֵĴ�Ƶ�ֵ����ͣ���Ϊ�������֣�ֵΪ������Ƶ��
#����֮����ϵ�̶ȵ��ֵ䣬��Ϊ��������������֣�ֵΪͬһ�г��ֵĴ�����

name={}   #key:name,value:f
connection={}#key;����,value:��һ���������ͬ�д���
NameLine=[]
#��ȡ�ļ�����ÿһ�н��ж�ȡ��

with open('���������Ľֵ�.txt') as f:
    for line in f.readlines():
# ��ȡ֮�����ʹ��jieba��ִʴ���jieba.cut()��������ִַʡ�
#Jieba�����ִַ�ģʽ��jieba.cut(  , cut_all=True),jieba.cut(  ,cut_all=False),jieba.cut_for_search(),cutǰ��l����б�jeba.lcut����
#�ڶ��ַ����Ϻ÷ִ�
        nameline=psg.cut(line)#��ע����
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
#node���������������Ƶ�ʼ�Ȩ�أ�������б�ʾ��Ĵ�С����edge�������ĳ��������֮����ϵ�����������������ֵ��Ǳ����ߵ��߿�

#�õ��������Ƶ
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
#edge:���������ϵ�̶�
#���ı����������.csv�ļ���
#����������ϵ