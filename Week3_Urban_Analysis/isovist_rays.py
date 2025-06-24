import Rhino.Geometry as geo
import scriptcontext as sc
import math

center = geo.Point3d(0, 0, 0)
for i in range(36):
    angle = math.radians(i * 10)
    dir = geo.Vector3d(math.cos(angle), math.sin(angle), 0)
    line = geo.Line(center, dir * 100)
    sc.doc.Objects.AddLine(line)
