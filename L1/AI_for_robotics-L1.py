# Lesson 1 of Artificial Intelligence for Robotics by Sebastian Thrun

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
    for entry in range(len(p)):
    	hit = (Z == world[i])
        q.append(p[entry] * (hit * pHit + (1-hit) * pMiss))
    qSum = sum(q)
    for entry in range(len(q)):
    	q[entry] = q[entry] / qSum
    return q


print (sense(p,Z))