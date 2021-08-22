import csv

content = open("Purp_EXP.csv", "r").read().replace('\r','\n')

with open("Purp2_EXP.csv", "w") as g:
    g.write(content)
