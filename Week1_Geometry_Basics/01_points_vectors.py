import Rhino.Geometry as geo
import scriptcontext as sc
import Rhino

base = geo.Point3d(0, 0, 0)
vec = geo.Vector3d(10, 5, 3)
moved = base + vec
sc.doc.Objects.AddPoint(base)
sc.doc.Objects.AddPoint(moved)
