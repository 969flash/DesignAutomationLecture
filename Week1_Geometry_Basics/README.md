# Week 1 - Geometry Basics (기하학적 기초)

## 개요
RhinoPython의 기본 지오메트리 객체 생성과 변환을 학습합니다.

## 학습 목표
- Rhino.Geometry 모듈의 기본 구조 이해
- Point3d, Vector3d, Curve, Surface, Brep 객체 생성
- 지오메트리 변환(Translation, Rotation, Scale) 적용
- scriptcontext를 통한 Rhino 문서 연동

## 실습 파일

### 1. 01_points_vectors.py / 01_points_vectors.ghx
**포인트와 벡터 기초**
- Point3d 객체 생성
- Vector3d 객체 생성  
- 벡터 연산을 통한 점 이동
- Rhino 뷰포트에 지오메트리 추가

### 2. 02_curves_surfaces.py / 02_curves_surfaces.ghx
**커브와 서페이스 생성**
- 수학적 함수로부터 점 생성
- NURBS 커브 생성
- 돌출(Extrusion)을 통한 서페이스 생성
- 커브와 서페이스를 Rhino에 추가

### 3. 03_brep_transform.py / 03_brep_transform.ghx
**Brep 객체와 변환**
- 기하학적 프리미티브(구)로부터 Brep 생성
- 변환 매트릭스 생성
- Brep 복제 및 변환 적용
- 원본과 변환된 객체 동시 표시

### 통합 파일: Week1_all.ghx
위 세 개의 Grasshopper 예제를 하나의 파일에 모아둔 버전입니다. `Week1_all.ghx` 파일을 열면
각 예제 그룹이 순차적으로 배치되어 있어 한 번에 모든 스크립트를 확인할 수 있습니다.

## 사용 방법

### Python 스크립트 실행
1. Rhino에서 EditPythonScript 명령 실행
2. 해당 .py 파일 열기
3. F5 키로 실행

### Grasshopper 파일 사용
1. Grasshopper 실행
2. 해당 .ghx 파일 열기
3. Python Script 컴포넌트의 코드 확인
4. 필요시 입력값 조정 후 실행

## 주요 개념
- **Point3d**: 3차원 공간의 점
- **Vector3d**: 방향과 크기를 가진 벡터
- **NurbsCurve**: Non-Uniform Rational B-Spline 커브
- **Surface**: 3차원 표면
- **Brep**: Boundary Representation (경계 표현법)
- **Transform**: 지오메트리 변환 매트릭스
