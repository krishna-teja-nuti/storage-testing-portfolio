import os
from datetime import datetime
from run_command import run_command

RESULTS_DIR = "results/s03_results"
os.makedirs(RESULTS_DIR, exist_ok=True)
LOG_FILE = os.path.join(RESULTS_DIR, "s03_test.log")

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

def save_output(filename, content):
    with open(os.path.join(RESULTS_DIR, filename), "w") as f:
        f.write(content)

def test_s03_create_file():
    run_command(["dd", "if=/dev/zero", "of=/teststorage/auto_test_file", "bs=1M", "count=10"])
    exists = os.path.exists("/teststorage/auto_test_file")
    if exists:
        log("test_s03_create_file PASSED - 10MB test file created successfully")
    else:
        log("test_s03_create_file FAILED - test file was not created")
    assert exists, "Test file was not created"

def test_s03_sparse_file_behavior():
    run_command(["dd", "if=/dev/zero", "of=/teststorage/auto_sparse_file", "bs=1M", "count=0", "seek=500"])
    apparent_size = os.path.getsize("/teststorage/auto_sparse_file")
    expected_size_mb = 500
    expected_size_bytes = expected_size_mb * 1024 * 1024
    apparent_size_mb = apparent_size / (1024 * 1024)
    du_output = run_command(["du", "-sh", "/teststorage/auto_sparse_file"])
    save_output("sparse_file_du_output.txt", du_output)
    size_ok = apparent_size == expected_size_bytes
    actual_minimal = "0" in du_output.split()[0]
    if size_ok and actual_minimal:
        log(f"test_s03_sparse_file_behavior PASSED - apparent: {apparent_size_mb:.1f}MB, actual: {du_output.strip()}")
    else:
        log(f"test_s03_sparse_file_behavior FAILED - apparent: {apparent_size_mb:.1f}MB, actual: {du_output.strip()}")
    assert size_ok, f"Expected {expected_size_mb}MB, got {apparent_size_mb:.1f}MB"
    assert actual_minimal, f"Expected near-zero actual disk usage, got {du_output}"

def test_s03_filesystem_full_behavior():
    run_command(["bash", "-c", "dd if=/dev/zero of=/teststorage/auto_bigfile bs=1M 2>/dev/null"], timeout=120)
    df_after = run_command(["df", "-h", "/teststorage"])
    save_output("filesystem_full_output.txt", df_after)
    run_command(["rm", "-f", "/teststorage/auto_bigfile"])
    is_full = "100%" in df_after
    if is_full:
        log("test_s03_filesystem_full_behavior PASSED - filesystem reached 100%")
    else:
        log(f"test_s03_filesystem_full_behavior FAILED - did not reach 100%: {df_after}")
    assert is_full, f"Expected filesystem to reach 100%, got: {df_after}"