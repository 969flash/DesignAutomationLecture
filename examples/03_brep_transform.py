import Rhino.Geometry as geo
import scriptcontext as sc

sphere = geo.Sphere(geo.Point3d(0,0,0), 5)
brep = geo.Brep.CreateFromSphere(sphere)
xform = geo.Transform.Translation(10, 0, 0)
brep_x = brep.Duplicate()
brep_x.Transform(xform)
sc.doc.Objects.AddBrep(brep)
sc.doc.Objects.AddBrep(brep_x)
