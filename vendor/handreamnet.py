import re
from netmiko import ConnectHandler

class handreamnet_switch:
    def __init__(self, deviceConnectionInfo):
        self.deviceConnectionInfo = deviceConnectionInfo

    def connect_to_switch(self):
        try:
            connection = ConnectHandler(**self.deviceConnectionInfo)
            connection.send_command_timing('enable')
            connection.send_command_timing(self.deviceConnectionInfo['secret'])
            connection.send_command_timing('terminal length 0')
            print(f"{self.deviceConnectionInfo['ip']}: 연결 성공")
            return connection
        except Exception as e:
            print(f"{self.deviceConnectionInfo['ip']}: 연결 실패 - {e}")

    def hostname(self, data):
        hostname = re.search(r'hostname\s+(\S+)', data)
        if hostname:
            return hostname.group(1)
        else:
            print(f"{self.deviceConnectionInfo['ip']}: 호스트네임 파싱 실패")
            return
    
    def fan_status(self, data):
        fan_patterns = [
        r"Fan\s*+is\s*(\w+)",
        r"System\s*+Fan\s*:\s*(\w+)",
        r"Status\s*:\s*(\w+)",
        ]
        
        for pattern in fan_patterns:
            match = re.search(pattern, data)
            if match:
                return match.group(1)
        print(f"{self.deviceConnectionInfo['ip']}: 팬 상태 파싱 실패")
        return 
    
    def temperature(self, data):
        temperature = re.search(r"M/B\s*Temp\s*:\s*(\d+\.\d+)", data)
        if temperature:
            return temperature.group(1)
        if not temperature:
            print(f"{self.deviceConnectionInfo['ip']}: 온도 파싱 실패")
            return 
    
    def uptime(self, data):
        uptime = re.search(r"up\s+(.+?),", data)
        if uptime:
            return uptime.group(1)
        if not uptime:
            print(f"{self.deviceConnectionInfo['ip']}: 업타임 파싱 실패")
            return 
    
    def cpu_usage(self, data):    
        cpu_usage = re.search(r"5\s+sec\s+:\s+([\d.]+)", data)
        if cpu_usage:
            return cpu_usage.group(1)
        if not cpu_usage:
            print(f"{self.deviceConnectionInfo['ip']}: CPU 사용량 파싱 실패")
            return 
    
    def memory_usage(self, data):
        used_match = re.search(r"Used\s*:\s*(\d+)\s+kB", data)
        usage_match = re.search(r"Current\s+memory\s+usage\s+:\s+(\d+\.\d+)", data)
        
        if used_match:
            return used_match.group(1)
        elif usage_match:
            return usage_match.group(1)
        else:
            print(f"{self.deviceConnectionInfo['ip']}: 메모리 사용량 파싱 실패")
            return 