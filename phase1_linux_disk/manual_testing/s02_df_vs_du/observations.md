# S02 — Disk Usage Deep Dive (df vs du) — Observations

## Scenario Simulated
Created a 500MB file (`openfile.dat`) on `/teststorage`, opened it with `tail -f` 
(PID 10782), then deleted it while still open — simulating a real production 
"deleted but open file" scenario.

## Mismatch Observed
- `df -h /teststorage` → 803M used
- `du -sh /teststorage` → 301M used
- **Discrepancy: ~500M** — matching the exact size of the deleted file

## Root Cause Investigation
Used `lsof | grep deleted` to identify the process still holding the file open:


Confirmed the `tail` process (PID 10782) was holding a file descriptor open 
to the deleted file, accounting for the full 500MB (524288000 bytes).

## Resolution — Production-Safe Method
Instead of killing the process (which would be risky for a real production 
process like a database), truncated the file descriptor directly:
```bash
sudo bash -c "> /proc/10782/fd/6"
```
This freed the disk space immediately without interrupting the running process.

## Verification
After truncation:
- `df -h /teststorage` → back to 303M (normal)
- `du -sh /teststorage` → 301M (matches df again)

Process was then safely terminated with `sudo kill 10782` for cleanup since 
this was a test scenario.

## Key Learning
A df vs du mismatch is one of the most common real-world storage discrepancies. 
`lsof | grep deleted` is the primary diagnostic tool, and truncating via 
`/proc/<PID>/fd/<FD>` is the safest fix when the holding process cannot be 
restarted (e.g., production databases).
