# Jira Ticket — S01 Disk Identification

**Ticket Type:** Test Finding / Observation
**Priority:** Low
**Status:** Closed - No Action Needed

## Summary
Verified disk identification consistency across lsblk, fdisk, blkid, and hwinfo 
on a 2-disk Linux VM (sda, sdb).

## Test Steps
1. Run `lsblk` — list all block devices
2. Run `sudo fdisk -l` — verify partition tables
3. Run `sudo blkid` — verify UUID and filesystem type
4. Run `sudo hwinfo --disk` — verify hardware details
5. Cross-validate all 4 outputs for consistency

## Expected Result
All commands should report consistent disk size, partition info, and filesystem 
type for each disk.

## Actual Result
All 4 commands returned consistent information. No mismatches found.
- sda: 40G, GPT, ext4
- sdb: 10G, MBR/DOS, ext4

## Observation (Notable Finding)
sda uses GPT partition table while sdb uses legacy MBR (DOS) partition table — 
both coexist without issue on the same system. This is a useful real-world 
example to demonstrate understanding of both partition table types.

## Evidence Attached
- lsblk_output.txt
- fdisk_output.txt
- blkid_output.txt
- hwinfo_output.txt

## Verdict
PASS — No discrepancies found across disk identification tools.
