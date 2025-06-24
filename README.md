# 자동화설계 특강 - RhinoPython & 한국 필지 기반 지오메트리 설계

RhinoPython과 한국 필지(GIS) 데이터를 활용한 자동화설계 실습 강의입니다. 기초 문법부터 도시분석 응용까지 5주에 걸쳐 학습합니다. 본 강의는 Rhino 8의 CPython 환경을 기준으로 구성됩니다.

## 프로젝트 구조

```
DesignAutomationLecture/
├── Week1_Geometry_Basics/          # 1주차: 기하학적 기초
│   ├── 01_points_vectors.py        
│   ├── 01_points_vectors.ghx       # Grasshopper 파일
│   ├── 02_curves_surfaces.py       
│   ├── 02_curves_surfaces.ghx      
│   ├── 03_brep_transform.py        
│   ├── 03_brep_transform.ghx       
│   └── README.md                   
├── Week2_GIS_Integration/          # 2주차: GIS 데이터 연동
│   ├── match_parcels_buildings.py  
│   ├── match_parcels_buildings.ghx 
│   └── README.md                   
├── Week3_Urban_Analysis/           # 3주차: 도시 분석
│   ├── isovist_rays.py             
│   ├── isovist_rays.ghx            
│   ├── urban_block_segmentation.py 
│   ├── urban_block_segmentation.ghx
│   └── README.md                   
├── Week4_Parcel_Analysis/          # 4주차: 필지 분석
│   ├── mass_by_parcel.py           
│   ├── mass_by_parcel.ghx          
│   └── README.md                   
├── Week5_Advanced_Terrain/         # 5주차: 고급 지형 분석
│   ├── view_slope_adjust.py        
│   ├── view_slope_adjust.ghx       
│   └── README.md                   
├── examples/                       # 원본 예제 파일들 (참고용)
│   └── ...                         
└── README.md                       # 이 파일
```

## 주차별 학습 내용

### Week 1 - Geometry Basics (기하학적 기초)
- RhinoPython 개발 환경 및 기본 문법
- Point3d, Vector3d, Curve, Surface, Brep 객체 생성
- 지오메트리 변환(Translation, Rotation, Scale)
- scriptcontext를 통한 Rhino 문서 연동

### Week 2 - GIS Integration (GIS 데이터 연동)  
- 국토지리정보원 수치지형도 SHP 데이터 활용
- pyshp 라이브러리를 통한 Shapefile 읽기
- 필지와 건축물 데이터 공간 매칭
- GIS 좌표를 Rhino 지오메트리로 변환

### Week 3 - Urban Analysis (도시 분석)
- 아이소비스트(Isovist) 시각 분석
- 방사형 레이 패턴 생성
- 도시 블록 세분화 및 중심점 계산
- 시각적 분석을 위한 기하학적 도구

### Week 4 - Parcel Analysis (필지 분석)
- CSV 데이터 기반 지오메트리 생성
- 필지 면적에 따른 건축 볼륨 계산
- 데이터 기반 설계 방법론
- 파라메트릭 높이 조절 시스템

### Week 5 - Advanced Terrain (고급 지형 분석)
- 지형 경사도에 반응하는 건축 설계
- 높이 조절을 통한 시야 확보
- 지형 적응형 파라메트릭 디자인
- 환경 요소를 고려한 건축 배치

## 사용 방법

### Python 스크립트 실행
1. Rhino 8 실행
2. `EditPythonScript` 명령 실행
3. 각 주차별 폴더의 .py 파일 열기
4. F5 키로 스크립트 실행

### Grasshopper 파일 실행
1. Grasshopper 실행
2. 각 주차별 폴더의 .ghx 파일 열기
3. Python Script 컴포넌트의 코드 확인
4. 필요시 입력 파라미터 조정 후 실행

## 필요 환경
- **Rhino 8**: CPython 환경 지원
- **Grasshopper**: Rhino 8에 포함
- **Python 패키지**: 
  - `pyshp` (Week 2에서 필요)
  - 기본 Python 라이브러리들 (csv, math 등)

## 설치 방법
```python
# Rhino 8 CPython 환경에서
# r: pyshp
import shapefile
```

weeks:

  - title: Week 1 - RhinoPython 기초 및 지오메트리 생성
    description: RhinoPython의 개발 환경과 기본 문법, 지오메트리 객체(Point, Curve, Surface, Brep) 생성 및 벡터 연산, 변환(이동, 회전, 스케일)을 활용한 반복 패턴 설계를 포괄적으로 학습합니다.
    modules:
      - title: Rhino.Geometry 기본 구조 및 객체 생성
        type: reading
        content: |
          Rhino.Geometry 모듈을 통해 Rhino 내부 지오메트리 객체를 생성합니다. 본 수업에서는 geo.Point3d, geo.Vector3d, geo.Polyline, geo.NurbsCurve, geo.Surface, geo.Brep 등의 객체를 실습합니다. 각 객체는 scriptcontext를 통해 Rhino 뷰포트에 시각화합니다.
      - title: 실습 코드 예제
        type: coding
        files:
          - name: examples/01_points_vectors.py
            content: |
              import Rhino.Geometry as geo
              import scriptcontext as sc
              import Rhino

              base = geo.Point3d(0, 0, 0)
              vec = geo.Vector3d(10, 5, 3)
              moved = base + vec
              sc.doc.Objects.AddPoint(base)
              sc.doc.Objects.AddPoint(moved)
          - name: examples/02_curves_surfaces.py
            content: |
              import Rhino.Geometry as geo
              import scriptcontext as sc

              pts = [geo.Point3d(i, i*i*0.1, 0) for i in range(-5, 6)]
              curve = geo.NurbsCurve.Create(False, 3, pts)
              sc.doc.Objects.AddCurve(curve)

              rail = geo.Line(geo.Point3d(0,0,0), geo.Point3d(0,0,10)).ToNurbsCurve()
              surface = geo.Surface.CreateExtrusion(curve, geo.Vector3d(0,0,5))
              sc.doc.Objects.AddSurface(surface)
          - name: examples/03_brep_transform.py
            content: |
              import Rhino.Geometry as geo
              import scriptcontext as sc

              sphere = geo.Sphere(geo.Point3d(0,0,0), 5)
              brep = geo.Brep.CreateFromSphere(sphere)
              xform = geo.Transform.Translation(10, 0, 0)
              brep_x = brep.Duplicate()
              brep_x.Transform(xform)
              sc.doc.Objects.AddBrep(brep)
              sc.doc.Objects.AddBrep(brep_x)

  - title: Week 2 - 한국 필지 GIS 연동 및 수치지형도 시각화
    description: 국토지리정보원의 수치지형도(2.0 버전, SHP 형식)를 Rhino에서 불러오고, 도로·건물·등고선 등 주요 지형 정보를 geo 기반 객체로 변환하여 시각화하며, 필지와 건축물 SHP 데이터를 공간적으로 매칭합니다.
    modules:
      - title: 수치지형도 SHP 데이터 전처리 및 불러오기 및 필지-건축물 매칭
        type: reading
        content: |
          국토지리정보원의 수치지형도 1:5000 (ver 2.0) SHP 데이터를 사용합니다. 주요 항목은 도로, 건물, 수계, 경계, 등고선 등이며, pyshp 패키지를 사용해 Rhino 8 CPython 환경에서 불러올 수 있습니다.

          또한, 필지정보(SHP)와 건축물대장정보(SHP)를 공간적으로 매칭하여, 각 필지에 어떤 건축물이 존재하는지 연결할 수 있습니다. 이를 위해 두 SHP 파일의 경계 정보를 비교하거나 중심점을 활용하여 공간 포함 여부를 판단합니다.

          Rhino 8에서는 아래와 같이 pyshp를 설치 및 임포트합니다:

          ```python
          # r: pyshp
          import shapefile

          sf = shapefile.Reader("TL_SPRD_BUILD.shp")
          for shape_rec in sf.shapeRecords():
              coords = shape_rec.shape.points
              # coords → geo.Point3d 변환 후 Polyline, Curve 등으로 활용
          ```

      - title: 실습 코드 예제
        type: coding
        files:
          - name: examples/match_parcels_buildings.py
            content: |
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

          - name: examples/mass_by_parcel.py
            content: |
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

  - title: Week 3 - 필지 조건 기반 자동 매스 생성
    description: CSV 또는 SHP 기반 필지데이터에 면적, 용도지역 등의 조건을 적용하여 자동화된 매스를 생성합니다.
    modules:
      - title: 필지 중심점, 면적 기반 매스 생성
        type: coding
        files:
          - name: examples/mass_by_parcel.py
            content: |
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

  - title: Week 4 - 뷰, 경사, 조망 조건을 고려한 지오메트리 최적화
    description: 주변의 지형 조건이나 조망 방향에 따라 자동으로 설계 형상이 조절되는 알고리즘을 구현합니다.
    modules:
      - title: 고도 및 조망 조건 기반 형상 생성
        type: coding
        files:
          - name: examples/view_slope_adjust.py
            content: |
              import Rhino.Geometry as geo
              import scriptcontext as sc

              base_pts = [geo.Point3d(x*10, 0, x*2) for x in range(10)]
              for pt in base_pts:
                  height = pt.Z * 0.8
                  box = geo.Box(geo.Plane(pt), geo.Interval(-2,2), geo.Interval(-2,2), geo.Interval(0,height))
                  sc.doc.Objects.AddBox(box)

  - title: Week 5 - 도시 단위 GIS 분석: Visibility 분석
    description: 경로를 따라 이동하는 사용자의 위치에서 Isovist(가시영역)를 생성하고 시각화합니다.
    modules:
      - title: 이동 경로 기반 Isovist 영역 생성
        type: coding
        files:
          - name: examples/isovist_rays.py
            content: |
              import Rhino.Geometry as geo
              import scriptcontext as sc
              import math

              center = geo.Point3d(0, 0, 0)
              for i in range(36):
                  angle = math.radians(i * 10)
                  dir = geo.Vector3d(math.cos(angle), math.sin(angle), 0)
                  line = geo.Line(center, dir * 100)
                  sc.doc.Objects.AddLine(line)

  - title: Week 6 - 도시공간 속 경계 인식과 분절 구조 분석
    description: 도시공간 내 물리적/인지적 경계(도로, 하천, 철도 등)에 의해 형성되는 블록 또는 클러스터를 자동 탐지하고, 공간 분절 구조를 분석합니다.
    modules:
      - title: 경계 객체 기반 블록 분할 및 중심점 추출
        type: coding
        files:
          - name: examples/urban_block_segmentation.py
            content: |
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
