#_____1_____
my_list=[7,8,9,2,3,1,4,10,5,6]

#_____2_____
lista=my_list.copy()
lista.sort()
print("Lista sortata ascendent->",lista)

#_____3_____
lista.sort(reverse = True)
print("Lista sortata descendent->",lista)

#_____4_____
lista.sort()
my_sliced_list=lista[1::2]
print("Numerele pare din lista sunt->",my_sliced_list)

#_____5_____
my_sliced_list2=lista[0::2]
print("Numerele impare din lista sunt->",my_sliced_list2)

#_____6_____
print("Elementele multipli ai lui 3->",)
for i in range(len(lista)):
    if my_list[i]%3==0:
        print(my_list[i])









