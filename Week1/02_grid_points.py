import rhinoscriptsyntax as rs
for i in range(5):
    for j in range(5):
        rs.AddPoint(i * 2, j * 2, 0)
