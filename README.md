# Virtual-Cybersecurity-Laboratory-and-Conducting-Android-Forensics-Investigations
 Android Forensics Investigations



# 🔐 Virtual Cybersecurity Laboratory and Android Forensics Investigation

## 📘 Project Overview

This project is the final capstone of a 3-month cybersecurity training program. It demonstrates the setup of a secure virtual cybersecurity lab and performs Android forensics using Python automation and SQLite database analysis.

---

## 🧩 Project Components

### ✅ Part I: Virtual Cybersecurity Lab Setup
- Installed and configured VirtualBox and VMware as Type-2 hypervisors.
- Created virtual machines:
  - **Kali Linux** (attacker environment)
  - **Windows 10** (target environment)
- Enabled internal networking between VMs.
- Verified connectivity using `ping`, file sharing, and port enumeration tools.

### ✅ Part II: Android Forensics Investigation
- Analyzed an Android `.img` file containing mock user data.
- Extracted evidence using Python and SQLite:
  - SMS Messages
  - Call Logs
  - Browser History
- Developed a Python GUI using `Tkinter` for viewing evidence in a structured, scrollable format.

### ✅ (Optional) Part III: Virtual Firewall (pfSense)
- Deployed pfSense firewall as a virtual appliance.
- Configured LAN/WAN, NAT, and basic port filtering.
- Routed Kali and Windows traffic through the firewall to test packet filtering and intrusion logging.

---

## 💻 Python Solution Features

- 📥 Extract SMS, calls, and browser history from `.db` files
- 📊 View data in a structured GUI using Tkinter tabs
- 🔍 Filter SMS by phone number
- 📤 Export data to CSV files
- 🔗 Clickable link to open the PDF Forensics Report

---

## 📂 Folder Structure

```bash
final_project_solution/
│
├── forensics_gui.py          # Main GUI application using Tkinter
├── sample_sms.db             # SQLite database with mock data
├── screenshots/              # Lab setup and GUI screenshots
├── reports/
│   └── Forensics_Report.pdf  # Final digital forensics report
├── firewall_config/          # (Optional) pfSense setup and rules
└── README.md                 # This file


#### Tools & Technologies
###### Tool	Purpose
- Python 3.10+	Backend scripting and GUI

- Tkinter	GUI interface for forensics

- SQLite3	Local database storage

- VirtualBox	Hypervisor for VM setup

- Autopsy	Android image analysis

- pfSense	Virtual firewall (optional)


#### Screenshots
Located in the screenshots/ folder:

- VirtualBox VM setup

- Autopsy analysis

- Python GUI showing SMS, call logs, browser history




#### Author
- Igbasan Olaniyi Marvin
Cybersecurity Enthusiast
