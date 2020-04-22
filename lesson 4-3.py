k=int(input("Введите размер массива:"))
import numpy as np
x=np.random.random(k)
print(x)
print("Среднее значение: " + str(np.mean(x)))
