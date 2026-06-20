# S01 — Disk Identification & Exploration — Observations

## Disks Found
- /dev/sda
- /dev/sdb

## Partition Table Type
- sda → GPT
- sdb → DOS/MBR

Both major partition table types found on the same system — confirms understanding 
of GPT vs MBR differences using the `fdisk -l` "Disklabel type" field.

## Disk Type (HDD vs SSD)
Checked via `/sys/block/<disk>/queue/rotational`:
- sda → 1 (HDD)
- sdb → 1 (HDD)

## Filesystem & UUID
Verified using `blkid` — both partitions formatted with ext4, each with a unique UUID.

## Hardware Details
Verified using `hwinfo --disk` — Model, Vendor, Serial ID, and Capacity confirmed 
for both disks.

## Cross-Validation
All 4 tools (lsblk, fdisk, blkid, hwinfo) returned consistent disk information — 
no mismatches.
