import matplotlib.pyplot as plt
import math

ress = [
"""
Array Size:1024 Arr_strides:4
Array Size Allocated: 4096 bytes
14.376200
Array Size:2048 Arr_strides:4
Array Size Allocated: 8192 bytes
13.067720
Array Size:4096 Arr_strides:4
Array Size Allocated: 16384 bytes
13.414880
Array Size:8192 Arr_strides:4
Array Size Allocated: 32768 bytes
14.449000
Array Size:16384 Arr_strides:4
Array Size Allocated: 65536 bytes
13.086200
Array Size:32768 Arr_strides:4
Array Size Allocated: 131072 bytes
13.558880
Array Size:65536 Arr_strides:4
Array Size Allocated: 262144 bytes
13.331400
Array Size:131072 Arr_strides:4
Array Size Allocated: 524288 bytes
13.095320
Array Size:262144 Arr_strides:4
Array Size Allocated: 1048576 bytes
13.258960
Array Size:524288 Arr_strides:4
Array Size Allocated: 2097152 bytes
13.323480
Array Size:1048576 Arr_strides:4
Array Size Allocated: 4194304 bytes
13.100240
Array Size:2097152 Arr_strides:4
Array Size Allocated: 8388608 bytes
14.239480
Array Size:4194304 Arr_strides:4
Array Size Allocated: 16777216 bytes
13.359200
""",

"""
Array Size:1024 Arr_strides:8
Array Size Allocated: 4096 bytes
13.689200
Array Size:2048 Arr_strides:8
Array Size Allocated: 8192 bytes
13.226920
Array Size:4096 Arr_strides:8
Array Size Allocated: 16384 bytes
13.071480
Array Size:8192 Arr_strides:8
Array Size Allocated: 32768 bytes
13.183040
Array Size:16384 Arr_strides:8
Array Size Allocated: 65536 bytes
13.525920
Array Size:32768 Arr_strides:8
Array Size Allocated: 131072 bytes
13.867240
Array Size:65536 Arr_strides:8
Array Size Allocated: 262144 bytes
13.175360
Array Size:131072 Arr_strides:8
Array Size Allocated: 524288 bytes
13.363080
Array Size:262144 Arr_strides:8
Array Size Allocated: 1048576 bytes
13.185960
Array Size:524288 Arr_strides:8
Array Size Allocated: 2097152 bytes
14.608520
Array Size:1048576 Arr_strides:8
Array Size Allocated: 4194304 bytes
14.780920
Array Size:2097152 Arr_strides:8
Array Size Allocated: 8388608 bytes
14.231560
Array Size:4194304 Arr_strides:8
Array Size Allocated: 16777216 bytes
15.361280
""",

"""
Array Size:1024 Arr_strides:16
Array Size Allocated: 4096 bytes
13.067760
Array Size:2048 Arr_strides:16
Array Size Allocated: 8192 bytes
13.066520
Array Size:4096 Arr_strides:16
Array Size Allocated: 16384 bytes
13.304840
Array Size:8192 Arr_strides:16
Array Size Allocated: 32768 bytes
13.957200
Array Size:16384 Arr_strides:16
Array Size Allocated: 65536 bytes
16.577120
Array Size:32768 Arr_strides:16
Array Size Allocated: 131072 bytes
16.792960
Array Size:65536 Arr_strides:16
Array Size Allocated: 262144 bytes
18.149680
Array Size:131072 Arr_strides:16
Array Size Allocated: 524288 bytes
16.677360
Array Size:262144 Arr_strides:16
Array Size Allocated: 1048576 bytes
16.674120
Array Size:524288 Arr_strides:16
Array Size Allocated: 2097152 bytes
17.191240
Array Size:1048576 Arr_strides:16
Array Size Allocated: 4194304 bytes
17.260240
Array Size:2097152 Arr_strides:16
Array Size Allocated: 8388608 bytes
21.118200
Array Size:4194304 Arr_strides:16
Array Size Allocated: 16777216 bytes
28.308560
""",

"""
Array Size:1024 Arr_strides:32
Array Size Allocated: 4096 bytes
14.383800
Array Size:2048 Arr_strides:32
Array Size Allocated: 8192 bytes
13.066400
Array Size:4096 Arr_strides:32
Array Size Allocated: 16384 bytes
13.299760
Array Size:8192 Arr_strides:32
Array Size Allocated: 32768 bytes
14.148200
Array Size:16384 Arr_strides:32
Array Size Allocated: 65536 bytes
17.358560
Array Size:32768 Arr_strides:32
Array Size Allocated: 131072 bytes
18.288280
Array Size:65536 Arr_strides:32
Array Size Allocated: 262144 bytes
17.865920
Array Size:131072 Arr_strides:32
Array Size Allocated: 524288 bytes
19.188920
Array Size:262144 Arr_strides:32
Array Size Allocated: 1048576 bytes
22.984080
Array Size:524288 Arr_strides:32
Array Size Allocated: 2097152 bytes
23.035600
Array Size:1048576 Arr_strides:32
Array Size Allocated: 4194304 bytes
24.186840
Array Size:2097152 Arr_strides:32
Array Size Allocated: 8388608 bytes
43.020200
Array Size:4194304 Arr_strides:32
Array Size Allocated: 16777216 bytes
72.652560
""",

"""
Array Size:1024 Arr_strides:64
Array Size Allocated: 4096 bytes
13.369760
Array Size:2048 Arr_strides:64
Array Size Allocated: 8192 bytes
13.747040
Array Size:4096 Arr_strides:64
Array Size Allocated: 16384 bytes
13.069840
Array Size:8192 Arr_strides:64
Array Size Allocated: 32768 bytes
14.153960
Array Size:16384 Arr_strides:64
Array Size Allocated: 65536 bytes
17.957200
Array Size:32768 Arr_strides:64
Array Size Allocated: 131072 bytes
16.684600
Array Size:65536 Arr_strides:64
Array Size Allocated: 262144 bytes
17.055240
Array Size:131072 Arr_strides:64
Array Size Allocated: 524288 bytes
39.467560
Array Size:262144 Arr_strides:64
Array Size Allocated: 1048576 bytes
32.255640
Array Size:524288 Arr_strides:64
Array Size Allocated: 2097152 bytes
32.169280
Array Size:1048576 Arr_strides:64
Array Size Allocated: 4194304 bytes
34.204280
Array Size:2097152 Arr_strides:64
Array Size Allocated: 8388608 bytes
87.237240
Array Size:4194304 Arr_strides:64
Array Size Allocated: 16777216 bytes
127.066320
"""
]

def divide_chunks(l, n): 
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

fig = plt.figure()
print(len(ress))
for res in ress:
	ax = fig.add_subplot(111)
	#print(res)
	lines = res.split("\n")
	lines = [l for l in lines if l.strip() != ""]
	X = []
	Y = []

	for c in divide_chunks(lines,3):
		X.append(int(c[1].split(": ")[1].split(" ")[0].strip()))
		Y.append(float(c[2]))

	X = [int(math.log2(x)) for x in X]

	#print(X)
	#print(Y)

	ax.plot(X, Y)


ax.annotate('32K L1', xy=(15, 20), xytext=(15, 40),
            arrowprops=dict(facecolor='black', shrink=0.05),
)
ax.annotate('256K L2', xy=(18, 30), xytext=(18, 50),
            arrowprops=dict(facecolor='black', shrink=0.05),
)
ax.annotate('4M L1', xy=(22, 50), xytext=(22, 90),
            arrowprops=dict(facecolor='black', shrink=0.05),
)
#plt.annotate( 15, 40, 0, -20, fc="k", ec="k", head_width=0.5, head_length=1, label="")
#plt.annotate( 18, 50, 0, -20, fc="k", ec="k", head_width=0.5, head_length=1, label="256K L2")
# plt.annotate( 22, 80, 0, -20, fc="k", ec="k", head_width=0.5, head_length=1, label="4M L3")
plt.show()

