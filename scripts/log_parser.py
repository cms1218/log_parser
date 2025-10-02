import os
import re


log_path = os.path.join('logs', 'sample_auth.log')
regex = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

ipDict = {}

with open (log_path, 'r') as log:
    content = log.readlines()
    for line in content:
        if re.search("Failed password", line):
            ip = (re.findall(regex, line))
            if ip[0] in ipDict:
                ipDict[ip[0]] += 1
            else:
                ipDict[ip[0]] = 1
            
with open ('failed_attempts_log.txt', 'w') as log:
    log.write(str(ipDict))