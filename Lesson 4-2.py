k=int(input("Введите размер массива:"))
import numpy as np
x=np.array (range(k))
print("Сумма значений массива составит: " + str(np.sum(x)))
