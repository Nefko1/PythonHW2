"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке Nefko,
новые имена придумайте самостоятельно.
"""
import os
for i in range(2, 11, 2):
    old = f"C:\PycharmProjects\pythonProject2\PythonTasks/ModuleOS/Nefko/{i}"
    new = f"C:\PycharmProjects\pythonProject2\PythonTasks/ModuleOS/Nefko/am_{i}"
    os.rename(old, new)