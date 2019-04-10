

urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

# get unique file name
f = [ x.split('/')[-1] for x in urls]
files = list(set(f)) 

dic = dict(zip(files,[0 for x in xrange(len(files))]))

for fn in f:
	dic[fn] += 1

counts = list(dic.values())
counts.sort(reverse=True)
counts = counts[0:3]

# number of interest is 3, the list is truncated to 3 elements, let's go through
processed = 0

for k in dic:
	try:
		if dic[k] ==  counts[processed]:
			processed += 1
			print "%s:%d" % (k,dic[k])
	except Exception,e:
			break
			





