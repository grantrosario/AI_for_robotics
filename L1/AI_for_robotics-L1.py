# Lesson 1 of Artificial Intelligence for Robotics by Sebastian Thrun

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q = []
    for entry in range(len(p)):
    	hit = (Z == world[entry])
    	q.append(p[entry] * (hit * pHit + (1-hit) * pMiss))
    qSum = sum(q)
    for entry in range(len(q)):
    	q[entry] = q[entry] / qSum
    return q

def move(p, U):
	q = []
	for i in range(len(p)):
		s = pExact * p[(i - U) % len(p)]
		s = s + pOvershoot * p[(i-U-1) % len(p)]
		s = s + pUndershoot * p[(i-U+1) % len(p)]
		q.append(s)
	return q

# for k in range(len(measurements)):
# 	p = sense(p, measurements[k])

print move(p, 1)

