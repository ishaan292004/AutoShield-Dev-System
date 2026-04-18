import time
import os

log_file = "/var/log/auth.log"
failed_attempts = {}

while True:
    with open(log_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        if "Failed password" in line:
            ip = line.split()[-1]

            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

            if failed_attempts[ip] > 10:
                print(f"⚠️ Attack detected from {ip}")
                os.system(f"bash response/block_ip.sh {ip}")

    time.sleep(10)