import rhinoscriptsyntax as rs
import random
for i in range(50):
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    rs.AddPoint(x, y, 0)
