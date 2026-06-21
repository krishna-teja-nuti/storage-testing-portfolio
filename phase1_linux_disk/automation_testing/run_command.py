import subprocess
import logging

def run_command(command, timeout=30):
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
        return result.stdout
    except subprocess.TimeoutExpired:
        logging.error(f"{' '.join(command)} timed out after {timeout} seconds")
        return ""
    except Exception as e:
        logging.error(f"{' '.join(command)} failed with error: {str(e)}")
        return ""