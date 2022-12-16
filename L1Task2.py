# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

print('Проверка истинности: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            left = not(x or y or z)
            right = not(x) and not(y) and not(z)
            if left == right:
                print(f'X = {x},Y = {y},Z = {z}: Результат совпадает и равен {left}')
            else:
                print(f'X = {x},Y = {y},Z = {z}: Результат не совпадает, слева {left}, справа {right}')