"""
Obtenha o maior número de um arquivo com 100000 numeros
(nums.txt usando o reduce
"""
import functools
print(functools.reduce(max, [n for n in open('nums.txt')]))
