"""
stdin = Standard input
stdout = Standard Output
stderr = Stantard error
"""

import sys

##### Streams - Conceito Básico #####
print("print('Ola stdout Mundo!'): ")
print('Ola stdout Mundo!')
input()

print("sys.stdout.write('Ola stdout Mundo!' + '\\n')")
sys.stdout.write('Ola stdout Mundo!' + '\n')
input()

print("input('Ola stdin Mundo!')")
input('Ola stdin Mundo!')
input()

print("print('Ola stdin Mundo!'); sys.stdin.readline()[:-1]")
print('Ola stdin Mundo!'); sys.stdin.readline()[:-1]
input()

