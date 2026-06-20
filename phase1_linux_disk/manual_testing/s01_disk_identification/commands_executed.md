# S01 — Commands Executed

## 1. List all block devices
```bash
lsblk
```
Lists all disks, partitions, sizes, and mount points.

## 2. Read partition table
```bash
sudo fdisk -l
```
Shows partition table type (GPT/MBR), sector details, and partition layout for each disk.

## 3. Get UUID and filesystem type
```bash
sudo blkid
```
Shows UUID and filesystem type for each formatted partition.

## 4. Identify HDD vs SSD
```bash
cat /sys/block/sda/queue/rotational
cat /sys/block/sdb/queue/rotational
```
Output `1` = HDD (rotational), `0` = SSD (non-rotational).

## 5. Get hardware details
```bash
sudo hwinfo --disk
```
Shows Model, Vendor, Serial ID, and Capacity for each physical/virtual disk.
