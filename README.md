# Storage Testing Portfolio

**Krishna Teja Nuti** | Aspiring Storage QA Engineer / SDET Storage

---

## About

Hands-on storage testing portfolio covering Linux storage internals, NFS/SMB/iSCSI 
protocols, RAID, NetApp ONTAP enterprise arrays, backup/recovery testing, and 
cloud/Kubernetes storage — built through a structured 52-session program combining 
**manual testing** and **Python/pytest automation**.

---

## Target Roles

| Priority | Role |
|----------|------|
| 1 | Storage QA Engineer / Storage Test Engineer |
| 2 | SDET - Storage / Test Automation Engineer |
| 3 | Storage Validation Engineer |
| 4 | NAS/SAN Test Engineer |
| 5 | Backup & Recovery QA Engineer / Data Protection Test Engineer |

---

## Repository Structure

storage-testing-portfolio/

│

├── phase1_linux_disk/

│   ├── manual_testing/        ← command outputs, observations, Jira-style bug reports

│   └── automation_testing/    ← Python scripts + pytest test suites

│

├── phase2_protocols/

├── phase3_reliability/

├── phase4_hardware_nvme/

├── phase5_netapp_ontap/

├── phase6_backup_recovery/

├── phase7_cloud_kubernetes/

└── phase8_framework/          ← master test runner, Jira API, HTML reports


Every phase follows the same pattern — manual evidence on one side, 
automated proof on the other.

---

## Phases & Sessions

| Phase | Sessions | Topic |
|-------|----------|-------|
| 1 | S01–S09 | Linux & Disk Fundamentals + Security |
| 2 | S10–S19 | Storage Protocols, Multipathing & Performance |
| 3 | S20–S27 | Reliability, Failure & Recovery Testing |
| 4 | S28–S31 | Hardware Storage & NVMe Testing |
| 5 | S32–S35 | Enterprise Storage Array Testing — NetApp ONTAP |
| 6 | S36–S41 | Backup, Recovery & Virtualized Storage |
| 7 | S42–S45 | Cloud & Kubernetes Storage Testing |
| 8 | S46–S49 | Full Automation Framework & Interview Prep |

---

## Core Skills

**Linux Storage** — disk/filesystem internals, LVM, RAID (mdadm), encryption (LUKS)
**Protocols** — NFS, SMB/CIFS, iSCSI, Fibre Channel, Multipathing
**Enterprise Arrays** — NetApp ONTAP CLI and REST API
**Performance** — fio benchmarking, iostat, IOPS/latency analysis
**Automation** — Python, subprocess, pytest, logging, JSON, regex
**Cloud** — AWS S3, EBS, Kubernetes PV/PVC/CSI
**Backup & Recovery** — RPO/RTO testing, Commvault/Veeam concepts

---

## Running the Automation Suite

```bash
cd phase1_linux_disk/automation_testing
pytest test_phase1.py
```

---

## Contact

GitHub: [krishna-teja-nuti](https://github.com/krishna-teja-nuti)
