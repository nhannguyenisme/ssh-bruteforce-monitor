# SSH Brute-force Monitoring System (HK2)

## 1. Introduction
This project implements a basic SSH brute-force monitoring system on Linux.
It analyzes system authentication logs to detect repeated failed SSH login attempts
and generates security alerts automatically.

The project is designed as a foundation for further development in later semesters.

---

## 2. Objectives
- Monitor SSH authentication activities on Linux
- Detect brute-force login attempts based on failed SSH logins
- Generate alert logs automatically
- Apply Linux service automation using systemd

---

## 3. Technologies Used
- Ubuntu Server
- OpenSSH (sshd)
- Python 3
- systemd service and timer
- Linux authentication logs (`/var/log/auth.log`)

---

## 4. System Overview
- SSH login attempts are recorded in `/var/log/auth.log`
- A Python script analyzes failed login attempts by IP address
- If the number of failures exceeds a threshold, an alert is generated
- The script runs automatically using a systemd timer

---

## 5. How It Works
1. SSH login failures are recorded by the system
2. The Python script scans authentication logs
3. Failed attempts are counted per IP address
4. Alerts are written to an alert log file
5. The process runs periodically without manual execution

---

## 6. Demonstration
- Generate multiple failed SSH login attempts
- The system detects abnormal behavior
- Alert messages are written to the alert log

---

## 7. Project Scope
This project focuses on **detection and monitoring only**.
Automated blocking or advanced response mechanisms are planned for future semesters.

---

## 8. Future Improvements
- Severity classification of attacks
- Automatic IP blocking
- Web-based monitoring dashboard
- Integration with notification systems

---

## 9. Author
Student: [Your Name]  
Major: Cybersecurity  
Semester: 2
