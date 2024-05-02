points = [(5,7), (1,5), (2,15), (3,4), (5,12), (20,55)]


def euclideanDistance (p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

distance = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance.append((points[i], points[j], euclideanDistance(points[i], points[j])))

min_distance = distance[0]
for d in distance:
    if d[2] < min_distance[2]:
        min_distance = d

print(min_distance)
