import csv
import rhinoscriptsyntax as rs
with open('parcels.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        area = float(row['area'])
        center = eval(row['center'])
        height = area / 10
        rs.AddBox(rs.BoundingBox([center, [center[0]+10, center[1]+10, height]]))
