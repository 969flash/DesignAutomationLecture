import csv
import Rhino.Geometry as geo
import scriptcontext as sc

with open('parcels.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        center = geo.Point3d(*eval(row['center']))
        area = float(row['area'])
        height = area * 0.1
        box = geo.Box(geo.Plane(center), geo.Interval(-5,5), geo.Interval(-5,5), geo.Interval(0,height))
        sc.doc.Objects.AddBox(box)
