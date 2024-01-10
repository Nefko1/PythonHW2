"""
Создайте программу создающую папку Nefko внутри которой еще 10 папок имена которых цифры от 1 до 10
"""
import os
os.mkdir("Nefko")
for i in range(1, 11):
    os.mkdir(f"C:/PycharmProjects/pythonProject2/PythonTasks/ModuleOS/Nefko/{i}")