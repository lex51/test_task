#!/usr/bin/env python3

#TODO Написать скрипт для сравнения двух списков с указанием что добавилось в список, что ушло, насколько позиций произошло смещение элемента в списке. Порядок элементов важен.
# Список 1: A, B, C, D, E, F, G, H, I, J, K, L, M, N
# Список 2: B, C, D, A, F, E, Z, M, N, J, K, L

# результат в виде ссылки на github
# Написать в телеграм @xinhuashe "Привет, я по поводу вакансии, вот моё решение тестового задания [ссылка на гитхаб]"
# Все вопросы также можно задать в телеграм

l1 = list(input())
l2 = list(input()) 

def diff(l1, l2):
    print('WARNING script dont\'t work with nonunicue elements in lists')
    print('original','\t', l1) 
    print('new', '\t\t', l2)
    print('aded elems','\t', ' '.join(set(l2) - set(l1)) )
    print('deleted elems', '\t', ' '.join(set(l1) - set(l2)) )

    for elem in set(l1) & set(l2): # goes only by common and unicue elements
        distance = l1.index(elem) - l2.index(elem) 
        left = True if distance  > 0  else False 
        print(f'element {elem} go {"left" if left is True else "right"} on {abs(distance)} positions') 
diff(l1, l2)