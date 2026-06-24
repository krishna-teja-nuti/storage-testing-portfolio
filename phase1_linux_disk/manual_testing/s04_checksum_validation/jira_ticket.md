# Jira Ticket — S04 Data Integrity & Checksum Validation

**Ticket Type:** Test Finding / Data Integrity Verification
**Priority:** High
**Status:** Closed - No Action Needed

## Summary
Validated data integrity using MD5, SHA256, and SHA512 checksums before and 
after file copy operation, and successfully detected simulated silent data 
corruption using checksum comparison.

## Test Steps
1. Created a 50MB test file using `dd`
2. Generated MD5, SHA256, SHA512 checksums of original file
3. Copied file using `cp`
4. Generated checksums of copied file
5. Compared hash values using `awk` + `diff` — confirmed integrity after copy
6. Injected 7 bytes of corruption at byte position 1024 using `dd conv=notrunc`
7. Regenerated checksum of corrupted file
8. Compared corrupted hash against original — confirmed corruption detected

## Expected Result
- Checksums of original and copy should be identical
- Checksums of corrupted file should differ from original
- Both scenarios should be clearly verifiable using diff

## Actual Result
- After copy: `diff hashes_before.txt hashes_after.txt` → empty (no differences) ✅
- After corruption: `diff hashes_before.txt hashes_corrupted.txt` → hash mismatch detected ✅

## Observation (Notable Finding)
Only 7 bytes changed out of 52,428,800 bytes (50MB) — yet all three checksums 
(MD5, SHA256, SHA512) immediately reflected the change. This confirms checksums 
are reliable for detecting even minimal silent data corruption.

## Evidence Attached
- checksums_before.txt
- checksums_after.txt
- hash_diff_output.txt (empty = integrity confirmed)
- checksums_corrupted.txt
- corruption_detected.txt

## Verdict
PASS — Checksum verification correctly confirmed integrity after copy and 
successfully detected simulated data corruption.
