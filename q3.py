

sum = 0
for x in xrange(1000):
	sum += x if (x % 3 == 0) or (x % 5 == 0) else 0


print sum