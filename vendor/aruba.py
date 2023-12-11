import re
from netmiko import ConnectHandler

class aruba_switch:
    def __init__(self, deviceConnectionInfo):
        self.deviceConnectionInfo = deviceConnectionInfo

    def connect_to_switch(self):
        try:
            connection = ConnectHandler(**self.deviceConnectionInfo)
            connection.send_command_timing('no page')
            print(f"{self.deviceConnectionInfo['ip']}: 연결 성공")
            return connection
        except Exception as e:
            print(f"{self.deviceConnectionInfo['ip']}: 연결 실패 - {e}")

    def hostname(self, data):
        hostname = re.search(r'System\s+Name\s+:\s+(.*)', data)
        if hostname:
            return hostname.group(1)
        else:
            print(f"{self.deviceConnectionInfo['ip']}: 호스트네임 파싱 실패")
            return
    
    def fan_status(self, data):
        fan_status = re.search(r'(\d+\s+/\s+\d+)\s+Fans\s+in\s+Failure\s+State', data)
        if fan_status:
            print(f"{self.deviceConnectionInfo['ip']}: 팬 상태 파싱 성공")
            return  fan_status.group(1)
        else:
            print(f"{self.deviceConnectionInfo['ip']}: 팬 상태 파싱 실패")
            return
    
    def temperature(self, data):
        temperature = re.search(r'Chassis\s+(\d+)', data)
        if temperature:
            return temperature.group(1)
        else:
            print(f"{self.deviceConnectionInfo['ip']}: 온도 파싱 실패")
            return 
    
    def uptime(self, data):
        uptime = re.search(r'Up\s+Time\s+:\s+(\d+\s+days)', data)
        if uptime:
            return uptime.group(1)
        else:
            print(f"{self.deviceConnectionInfo['ip']}: 업타임 파싱 실패")
            return 
    
    def cpu_usage(self, data):    
        cpu_usage = re.search(r'CPU\s+Util\s+\(%\)\s+:\s+(\d+)', data)
        if cpu_usage:
            return cpu_usage.group(1)
        else:
            print(f"{self.deviceConnectionInfo['ip']}: CPU 사용량 파싱 실패")
            return 
    
    def memory_usage(self, data):
        memory_usage = re.search(r'Memory\s+-\s+Total\s+:\s+(.*)', data)
        if memory_usage:
            return memory_usage.group(1)
        else:
            print(f"{self.deviceConnectionInfo['ip']}: 메모리 사용량 파싱 실패")
            return 