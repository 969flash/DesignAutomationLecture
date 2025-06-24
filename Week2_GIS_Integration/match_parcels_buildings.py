# r: pyshp
import shapefile
import Rhino.Geometry as geo
import scriptcontext as sc

parcel_sf = shapefile.Reader("TL_PARCEL.shp")
building_sf = shapefile.Reader("TL_SPRD_BUILD.shp")

parcel_shapes = [(s.shape.points, s.record) for s in parcel_sf.iterShapeRecords()]
building_shapes = [(s.shape.points, s.record) for s in building_sf.iterShapeRecords()]

for p_coords, p_rec in parcel_shapes:
    p_poly = geo.Polyline([geo.Point3d(x, y, 0) for x, y in p_coords])
    p_brep = geo.Brep.CreatePlanarBreps(p_poly.ToNurbsCurve())
    matched = []
    for b_coords, b_rec in building_shapes:
        pt = geo.Point3d(b_coords[0][0], b_coords[0][1], 0)
        if p_brep and p_brep[0].IsPointInside(pt, 0.01, True):
            matched.append(b_rec)

    if matched:
        sc.doc.Objects.AddPolyline(p_poly)
