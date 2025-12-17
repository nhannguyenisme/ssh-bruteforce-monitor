from datetime import datetime

log_file = "/var/log/auth.log"
alert_file = "/home/devops/security_project/alerts.log"
threshold = 3

ip_counter = {}

with open(log_file, "r") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            parts = line.split()

            ip = None
            if "from" in parts:
                idx = parts.index("from")
                if idx + 1 < len(parts):
                    ip = parts[idx + 1]

            if ip:
                ip_counter[ip] = ip_counter.get(ip, 0) + 1

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

alerts = []
for ip, count in ip_counter.items():
    if count >= threshold:
        msg = f"[{now}] [ALERT] Possible brute-force from {ip} ({count} attempts)"
        alerts.append(msg)

if alerts:
    # In ra màn hình
    for a in alerts:
        print(a)

    # Ghi file (append)
    with open(alert_file, "a") as af:
        for a in alerts:
            af.write(a + "\n")
else:
    print(f"[{now}] No brute-force detected (threshold={threshold}).")

