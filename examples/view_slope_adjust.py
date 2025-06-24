import Rhino.Geometry as geo
import scriptcontext as sc

base_pts = [geo.Point3d(x*10, 0, x*2) for x in range(10)]
for pt in base_pts:
    height = pt.Z * 0.8
    box = geo.Box(geo.Plane(pt), geo.Interval(-2,2), geo.Interval(-2,2), geo.Interval(0,height))
    sc.doc.Objects.AddBox(box)
