import csv

f = open('converão.csv', 'w')
try:
    writer = csv.writer(f)
    writer.writerow( ('Celsius','F') )
    for i in range(0, 101, 10):
        writer.writerow( (i, 32 + i*1.8) )
finally:
    f.close()
