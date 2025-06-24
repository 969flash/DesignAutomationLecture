import Rhino.Geometry as geo
import scriptcontext as sc

blocks = [
    geo.Polyline([geo.Point3d(0,0,0), geo.Point3d(0,10,0), geo.Point3d(10,10,0), geo.Point3d(10,0,0), geo.Point3d(0,0,0)]),
    geo.Polyline([geo.Point3d(12,0,0), geo.Point3d(12,10,0), geo.Point3d(20,10,0), geo.Point3d(20,0,0), geo.Point3d(12,0,0)])
]

for blk in blocks:
    sc.doc.Objects.AddPolyline(blk)
    centroid = sum([pt for pt in blk], geo.Point3d(0,0,0)) / len(blk)
    sc.doc.Objects.AddPoint(centroid)
