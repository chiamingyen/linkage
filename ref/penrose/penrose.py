import sys
import lindenmayer
import turtle

print """usage: python penrose.py <n-steps>
generates a Penrose-tile linkage, based on n-steps
of the L-system for Pnerose tilings.
output is saved to default location of Linkage.save()"""

start = '[7]++[7]++[7]++[7]++[7]'
rules = \
{'6': '81++91----71[-81----61]++',\
'7': '+81--91[---61--71]+',\
'8': '-61++71[+++81++91]-',\
'9': '--81++++61[+91++++71]--71',\
'1': ''}

lind = lindenmayer.Lindenmayer(rules)
n = int(sys.argv[1])
s = lind.iter(start,n)
print s

turt = turtle.Turtle(['1'],36,60,300,300)
link = turt.makeLinkage(s)
link.save()
