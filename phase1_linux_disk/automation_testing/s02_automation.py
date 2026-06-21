import os
from datetime import datetime
from run_command import run_command

RESULTS_DIR = "../results/s02_results"
os.makedirs(RESULTS_DIR, exist_ok=True)
LOG_FILE = os.path.join(RESULTS_DIR, "s02_test.log")

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

def save_output(filename, content):
    with open(os.path.join(RESULTS_DIR, filename), "w") as f:
        f.write(content)

def test_s02_df_command_works():
    output = run_command(["df", "-h", "/teststorage"])
    save_output("df_output.txt", output)
    if "/teststorage" in output:
        log("test_s02_df_command_works PASSED - df returned data for /teststorage")
    else:
        log("test_s02_df_command_works FAILED - no data for /teststorage")
    assert "/teststorage" in output, "df did not return data for /teststorage"

def test_s02_du_command_works():
    output = run_command(["du", "-sh", "/teststorage"])
    save_output("du_output.txt", output)
    if output.strip() != "":
        log(f"test_s02_du_command_works PASSED - du output: {output.strip()}")
    else:
        log("test_s02_du_command_works FAILED - empty output")
    assert output.strip() != "", "du returned empty output"

def test_s02_no_deleted_open_files():
    output = run_command(["sudo", "bash", "-c", "lsof 2>/dev/null | grep deleted | grep teststorage"])
    save_output("lsof_output.txt", output if output.strip() else "No deleted open files found - clean state")
    if output.strip() == "":
        log("test_s02_no_deleted_open_files PASSED - no deleted open files found")
    else:
        log(f"test_s02_no_deleted_open_files FAILED - found: {output.strip()}")
    assert output.strip() == "", f"Found deleted but open files holding space: {output}"