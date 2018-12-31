# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
ab=float(input())
bc=float(input())
tetha= math.degrees(math.atan(ab/bc))
print('{}'.format(str(int(round(tetha,0))))+"°")