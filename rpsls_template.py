#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��
    
    if name=="ʯͷ":
         number=0
    elif name=="ʷ����":
         number=1
    elif name=="ֽ":
         number=2
    elif name=="����":
         number=3
    elif name=="����":
         number=4
    else:
         print("Error: No Correct Name") 
    return number

		

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

     #��дִ�д���,������ɺ�passɾ��
    if number==0:
         name="ʯͷ"
    elif number==1:
         name="ʷ����"
    elif number==2:
         name="ֽ"
    elif number==3:
         name="����"
    else:
        name="����"
    return name


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    #����������ʾ��дִ�д��룬������ɺ�ɾ����pass
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    a=number_to_name(comp_number)
    print("������ѡ��Ϊ%s"%a)
    if player_choice_number==comp_number:
       print("���ͼ��������һ����")
    elif (comp_number==(4 or 3)) and player_choice_number==0:
        print("��Ӯ��")
    elif (comp_number==(0 or 4)) and player_choice_number==1:
        print("��Ӯ��")
    elif (comp_number==(0 or 1)) and player_choice_number==2:
        print("��Ӯ��")
    elif (comp_number==(1 or 2)) and player_choice_number==3:
        print("��Ӯ��")
    elif (comp_number==(3 or 2)) and player_choice_number==4:
        print("��Ӯ��")
    else:
        print("�����Ӯ��")
    

# �Գ�����в���

print("��ӭʹ��RPSLS��Ϸ")
while True:
   print("----------------")
   print("����������ѡ��:")
   choice_name=str(input())
   if choice_name not in["ֽ","����","ʷ����","����","ʯͷ"]:
        print("Error: No Correct Name")
   else:
       print("����ѡ��Ϊ%s"%choice_name)
       rpsls(choice_name)


