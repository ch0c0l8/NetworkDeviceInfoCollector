# 네트워크 장비 모니터링 도구

## 개요
이 파이썬 스크립트는 다양한 스위치에 연결하여 관련 정보를 가져오고 데이터를 Excel 파일에 기록하는 네트워크 장비 모니터링 도구로 사용됩니다.
지원되는 장치에는 한드림넷과 아루바의 스위치가 포함됩니다.

## 기능

### 1. 연결 정보 구성
이 스크립트는 `device_connection_infos.txt`라는 파일에서 연결 정보를 읽습니다. 이 파일에는 각 장치에 대한 장치 유형, IP 주소, 포트, 사용자 이름, 비밀번호 및 활성 비밀번호와 같은 세부 정보가 포함되어 있습니다.
```plaintext
handreamnet,192.168.1.1,22,admin,password,enable_password
aruba_os,192.168.1.2,22,admin,password,enable_password
```

### 2. 장치 클래스
이 스크립트는 `handreamnet_switch` 및 `aruba_switch` 두 클래스를 정의합니다. 각각이 한드림넷 및 아루바 스위치에 해당하며 해당 장치에서 연결하고 특정 정보를 추출합니다.

### 3. 데이터 수집 및 구문 분석
각 연결된 장치에 대해 스크립트는 다음 작업을 수행합니다.
- 장치에 연결합니다.
- 실행 중인 구성 및 팬 상태, 온도, 업타임, CPU 사용량 및 메모리 사용량과 같은 특정 정보를 검색합니다.
- 정규 표현식을 사용하여 검색된 데이터에서 관련 정보를 추출합니다.

### 4. 기록 및 백업
스크립트는 수집된 데이터를 device_info.xlsx Excel 파일에 기록합니다. 또한 구성 파일 및 세션 로그를 위한 백업 폴더를 생성합니다.

## 사용법
1. device_connection_infos.txt라는 파일에 필요한 연결 세부 정보를 작성합니다.
2. 스크립트를 실행하면 각 장치에 연결하여 정보를 가져오고 `device_info.xlsx` Excel 파일에 기록합니다.
3. 연결 확인 및 데이터 검색에 대한 정보는 터미널 출력에서 확인할 수 있습니다.

## 요구 사항
Python 3.x
필수 Python 패키지: openpyxl, netmiko
```plaintext
pip install openpyxl netmiko
```
