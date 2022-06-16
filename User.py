from lab7.Gomory import *
from lab7.VetveyGranits import *



class User:
    def userAnswer(self):
        """
        Функция создана дл упрощения работы пользователя с данной программой, тут представлены подсказки и премеры ввода
        данных.
        Returns
        ===========
        Обращается к нужной функции метода и передает ей необходимые параметры.
        """
        print(
            "Каким методом хотите воспользоваться?\n"
            "1 - Функцию, решающую задачу целочисленного линейного программирования методом отсекающих плоскостей "
            "( Метод Гомори). \n"
            "2 - Функцию, решающую задачу целочисленного линейного программирования методом полного перебора "
            "( Метод ветвей и границ) \n ")


        user_answer = int(input())

        # Метод Гомори
        if user_answer == 1:
            print("Мы будем минимизировать или максимизировать ф-цию? Введите MAX или MIN:")
            mode = str(input())
            print("Введите список коэффициетов для иксов функции (4.00x1 + 5.00x2 + 6.00x3). Например: 4 5 6. \n "
                  "После завершения набора напишите end")
            c = []
            while True:
                s = input()
                if s == "end":
                    break
                row = [int(x) for x in s.split()]
                c.append(row)
            c = np.array(c)[0]

            print(f'Введите ограничения в формате коэффициетов для иксов. Например (после ввода \n '
                  f'каждой строки нажмите enter, а при завершении ввода напишите end): \n '
                  f'1 2 3 \n '
                  f'4 3 2 \n '
                  f'3 1 1 \n ')
            a = []
            while True:
                s = input()
                if s == "end":
                    break
                row = [int(x) for x in s.split()]
                a.append(row)
            a = np.array(a)
            print(f'Введите чему равняются ограничения в формате списка. Например: \n '
                  f'35 45 40 \n '
                  f'После завершения набора напишите end')
            b = []
            while True:
                s = input()
                if s == "end":
                    break
                row = [int(x) for x in s.split()]
                b.append(row)
            b = np.array(b)[0]

            Gomory_visualize(c, a, b, main(c, a, b, mode))

        # Метод ветвей и границ
        if user_answer == 2:
            print("Мы будем минимизировать или максимизировать ф-цию? Введите MAX или MIN:")
            mode = str(input())
            print("Введите список коэффициетов для иксов функции (4.00x1 + 5.00x2 + 6.00x3). Например: 4 5 6. \n "
                  "После завершения набора напишите end")
            c = []
            while True:
                s = input()
                if s == "end":
                    break
                row = [int(x) for x in s.split()]
                c.append(row)
            c = np.array(c)[0]

            print(f'Введите ограничения в формате коэффициетов для иксов. Например (после ввода \n '
                  f'каждой строки нажмите enter, а при завершении ввода напишите end): \n '
                  f'1 2 3 \n '
                  f'4 3 2 \n '
                  f'3 1 1 \n ')
            a = []
            while True:
                s = input()
                if s == "end":
                    break
                row = [int(x) for x in s.split()]
                a.append(row)
            a = np.array(a)
            print(f'Введите чему равняются ограничения в формате списка. Например: \n '
                  f'35 45 40 \n '
                  f'После завершения набора напишите end')
            b = []
            while True:
                s = input()
                if s == "end":
                    break
                row = [int(x) for x in s.split()]
                b.append(row)
            b = np.array(b)[0]

            VG_visualize(c, a, b, main(c, a, b, mode))
        else:
            print('Введен неверный номер')


# functionss = User()
# functionss.userAnswer()
