def mario(n):
    symb_1 = "#"
    symb_2 = " "
    k = 1
    while k != n+1:
        print(symb_2*(n-k), symb_1*k, symb_1*k, symb_2*(n-k))
        k += 1
    return


print(mario(8))

# def mario(n):
#     symb_1 = "#"
#     symb_2 = " "
#     k = 1
#     while k != n+1:
#         print(symb_2*(n-k), symb_1*k)
#         k += 1
#     return
#
#
# print(mario(8))




# if __name__ == '__main__':
#     if len(sys.argv) == 2:
#         n = int(sys.argv[1])
#     else:
#         n = 8
#     mario(n)



#
#
# # Данн размер препятствия n
# # Нужно построить конструкцию такой формы и высотой n:
#        #
#       ##
#      ###
#     ####
#    #####
#   ######
#  #######
# ########
#
#
# import sys
#
#
# def mario(n):
#     # your code here
#     pass
#
#
# if __name__ == '__main__':
#     if len(sys.argv) == 2:
#         n = int(sys.argv[1])
#     else:
#         n = 8
#     mario(n)





# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # устанавливаем имя
#         self.__age = age  # устанавливаем возраст
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
#
#     @property
#     def name(self):
#         return self.__name
#
#     def get_display_info(self):
#         return [
#             ['Имя', self.__name],
#             ['Возраст', str(self.__age)]
#         ]
#
#     def display_info(self):
#         res = self.get_display_info()
#         print('\n'.join([': '.join(el) for el in res]))
#
#
# class Employee(Person):
#
#     def details(self, company):
#         # print(self.__name, "работает в компании", company) # так нельзя, self.__name - приватный атрибут
#         print(self.name, "работает в компании", company)
#
#
# tom = Employee("Tom", 23)
# tom.details("Google")
# tom.age = -33
# tom.display_info()