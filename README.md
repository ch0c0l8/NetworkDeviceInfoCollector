# NetworkDeviceInfoCollector (네트워크 장비 정보 수집기)

## 개요
이 파이썬 스크립트는 다양한 스위치에 연결하여 관련 정보를 가져오고 데이터를 Excel 파일에 기록하는 네트워크 장비 점검 스크립트입니다.

## 기능
- **다양한 스위치 지원**: 한드림넷 스위치, Aruba 스위치 및 Cisco IOS 스위치를 지원합니다.
- **데이터 수집**: 팬 상태, 온도, 가동 시간, CPU 사용률 및 메모리 사용량을 수집하고 설정 파일을 백업합니다.
- **Excel 통합**: 수집된 데이터를 device_info.xlsx Excel 파일에 저장합니다.

## 사용 방법
1. **연결 정보 파일**: `device_connection_infos.txt` 텍스트 파일을 생성하여 장치 연결 세부 정보를 입력하세요. 각 줄에는 장치 유형, IP 주소, 포트, 사용자 이름, 비밀번호 및 활성 비밀번호가 쉼표로 구분되어 있어야 합니다.
```planetext
handreamnet,192.168.1.1,22,user,password,enable_password
aruba_os,192.168.1.2,22,user,password,enable_password
cisco_ios,192.168.1.3,22,user,password,enable_password
```
2. 스크립트 실행: 지정된 장치에 연결하여 정보를 수집하고 device_info.xlsx Excel 파일에 저장합니다.

## 필요 조건
- Python 3.x
- 필요한 Python 라이브러리: `openpyxl`, `netmiko`

## 설치
1. 리포지토리를 로컬로 복제합니다.
```bash
git clone https://github.com/your-username/network-device-info-collector.git
```
2. 필요한 Python 라이브러리를 설치합니다.
```bash
pip install openpyxl netmiko
```
3. 사용 방법 섹션에서 설명한대로 연결 정보 파일(device_connection_infos.txt)을 작성합니다.
4. 스크립트를 실행합니다.
```bash
python NetworkDeviceInfoCollector.py
```
