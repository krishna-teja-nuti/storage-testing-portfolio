import os
from datetime import datetime
from run_command import run_command

RESULTS_DIR = "../results/s01_results"
os.makedirs(RESULTS_DIR, exist_ok=True)
LOG_FILE = os.path.join(RESULTS_DIR, "s01_test.log")

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

def save_output(filename, content):
    with open(os.path.join(RESULTS_DIR, filename), "w") as f:
        f.write(content)

def test_s01_disk_count():
    output = run_command(["lsblk"])
    save_output("lsblk_output.txt", output)
    disks = []
    for line in output.splitlines():
        parts = line.split()
        if len(parts) >= 6 and parts[-1] == "disk":
            disks.append(parts[0])
    if len(disks) >= 2:
        log(f"test_s01_disk_count PASSED - Disks found: {disks}")
    else:
        log(f"test_s01_disk_count FAILED - Only found: {disks}")
    assert len(disks) >= 2, f"Expected >= 2 disks but found {len(disks)}: {disks}"

def test_s01_uuid_present():
    output = run_command(["sudo", "blkid"])
    save_output("blkid_output.txt", output)
    if "UUID=" in output:
        log("test_s01_uuid_present PASSED - UUID found")
    else:
        log("test_s01_uuid_present FAILED - No UUID found")
    assert "UUID=" in output, "No UUID found in blkid output"

def test_s01_partition_table_types():
    output = run_command(["sudo", "fdisk", "-l"])
    save_output("fdisk_output.txt", output)
    has_gpt = "gpt" in output.lower()
    has_dos = "dos" in output.lower()
    if has_gpt and has_dos:
        log("test_s01_partition_table_types PASSED - Both GPT and DOS found")
    else:
        log(f"test_s01_partition_table_types FAILED - GPT:{has_gpt} DOS:{has_dos}")
    assert has_gpt, "GPT partition table not found"
    assert has_dos, "DOS/MBR partition table not found"