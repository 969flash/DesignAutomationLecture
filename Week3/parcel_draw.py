import csv
import rhinoscriptsyntax as rs
with open('parcels.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        coords = eval(row['boundary'])
        rs.AddPolyline(coords)
