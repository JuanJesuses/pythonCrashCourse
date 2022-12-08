from pizza_3 import *

pizza1 = (12, 'cosas', 'cosillas', 'cosacas')
pizza2 = (16, 'chicha', 'rulo', 'cabra', 'queso')
pizza3 = (18, 'arroz', 'soja', 'picante', 'york')
pizza4 = (22, 'grande', 'enorme')

todas = (pizza1, pizza2, pizza3, pizza4)

make_pizza(12, 'cosas', 'cosillas', 'cosacas')
make_pizza(pizza1[0], pizza1[1], pizza1[2], pizza1[3])

for pizza in todas:
    add_pizza(pizza)