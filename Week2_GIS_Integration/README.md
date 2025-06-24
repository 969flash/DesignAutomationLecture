# Week 2 - GIS Integration (GIS 데이터 연동)

## 개요
한국 필지 및 건축물 GIS 데이터(Shapefile)를 Rhino에서 불러와 공간 분석을 수행합니다.

## 학습 목표
- Shapefile 데이터 구조 이해
- pyshp 라이브러리를 통한 SHP 파일 읽기
- GIS 좌표를 Rhino 지오메트리로 변환
- 공간적 포함 관계 분석 (Point-in-Polygon)
- 필지와 건축물 데이터 매칭

## 실습 파일

### match_parcels_buildings.py / match_parcels_buildings.ghx
**필지-건축물 매칭 분석**
- 필지 Shapefile 데이터 읽기
- 건축물 Shapefile 데이터 읽기
- 필지 폴리곤 내부의 건축물 탐지
- 매칭된 필지만 Rhino에 시각화

## 필요한 데이터
- `TL_PARCEL.shp`: 필지정보 Shapefile
- `TL_SPRD_BUILD.shp`: 건축물대장정보 Shapefile

## 설치 요구사항
```python
# Rhino 8 CPython 환경에서
# r: pyshp
import shapefile
```

## 사용 방법

### Python 스크립트 실행
1. 필요한 SHP 파일들을 작업 디렉토리에 배치
2. Rhino에서 EditPythonScript 명령 실행
3. match_parcels_buildings.py 파일 열기
4. 파일 경로 확인 후 F5로 실행

### Grasshopper 파일 사용
1. SHP 파일 경로를 입력 컴포넌트에 연결
2. Python Script 컴포넌트 실행
3. 매칭된 필지 폴리곤 출력 확인

## 주요 개념
- **Shapefile**: GIS 벡터 데이터 표준 포맷
- **Point-in-Polygon**: 점이 폴리곤 내부에 있는지 판단하는 공간 분석
- **Spatial Matching**: 공간적 위치 관계를 통한 데이터 연결
- **GIS Coordinates**: 지리정보시스템의 좌표계
- **Polyline**: 연결된 선분들로 구성된 폴리곤

## 데이터 출처
- 국토지리정보원 수치지형도 1:5000 (ver 2.0)
- 필지정보 및 건축물대장정보
