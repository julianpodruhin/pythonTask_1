# This is a sample Python script.
import math
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

d1 = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды)=>"))
print(d1)
d2 = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы)=>"))
print(d2)
h = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды)=>"))
print(h)
v_sand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час)=>"))
print(v_sand)
n = float(input("Введите коэффициент замедления спасателя при движении в воде, n=>"))
print(n)
theta_1 = float(input("Введите направление движения спасателя по песку, theta1 (градусы) =>"))
print(theta_1)
theta_rad = (theta_1 * math.pi)/180
x = d1 * math.tan(theta_rad)
L_1 = math.sqrt(math.pow(x, 2) + math.pow(d1, 2))
L_2 = math.sqrt(math.pow((h - x), 2) + math.pow(d2, 2))
t = (L_1 + n * L_2) / v_sand 
print("Если спасатель начнёт движение под углом theta1, равным 39 градусам, он достигнет утопащего через", t)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
