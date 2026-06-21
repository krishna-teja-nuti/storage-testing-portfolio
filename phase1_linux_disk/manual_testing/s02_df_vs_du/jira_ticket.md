# Jira Ticket — S02 Disk Usage Deep Dive (df vs du)

**Ticket Type:** Test Finding / Investigation
**Priority:** Medium
**Status:** Closed - Resolved

## Summary
Investigated a 500MB discrepancy between `df -h` and `du -sh` output on 
`/teststorage`, caused by a deleted-but-open file held by a running process.

## Test Steps
1. Created a 500MB file `openfile.dat` on `/teststorage`
2. Opened the file with `tail -f` (kept a file descriptor open)
3. Deleted the file using `rm` while the process still held it open
4. Compared `df -h` vs `du -sh` output
5. Used `lsof | grep deleted` to identify the process holding the file
6. Freed the space via `/proc/<PID>/fd/<FD>` truncation (production-safe method)
7. Re-verified `df` and `du` showed consistent values after fix

## Expected Result
`df` and `du` should report consistent disk usage when there are no deleted-but-open files.

## Actual Result
- Before fix: `df` reported 803M used, `du` reported 301M used — 500M discrepancy
- Root cause confirmed via `lsof`: PID 10782 (`tail`) holding deleted file open, 524288000 bytes (500MB)
- After fix: both `df` and `du` reported ~301M — consistent

## Observation (Notable Finding)
Deleted-but-open files are a common, often misunderstood cause of `df` vs `du` 
mismatches in production. The safest remediation when the holding process 
cannot be restarted is truncating the file descriptor via `/proc/<PID>/fd/<FD>` 
rather than killing the process.

## Evidence Attached
- df_output.txt / du_output.txt (baseline)
- lsof_output.txt (root cause evidence)
- df_output_final.txt / du_output_final.txt (post-fix verification)

## Verdict
PASS — Root cause identified and resolved using production-safe method.
