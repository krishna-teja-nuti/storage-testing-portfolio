# S04 — Data Integrity & Checksum Validation — Observations

## Test File Created
Created a 50MB test file using `dd if=/dev/zero` on `/teststorage` for 
consistent, reproducible checksum testing.

## Checksums Generated (Before Operation)
Generated three checksums for the original file:
- MD5: 25e317773f308e446cc84c503a6d1f85
- SHA256: 8565a714dca840f8652c5bae9249ab05f5fb5a4f9f13fbe23304b10f68252da2
- SHA512: 50173936f83822c28812ea23f7f843a27e8b85f65626cbc339...

## Integrity Verification After Copy
Copied the file using `cp` and regenerated checksums on the copy.
Extracted only hash values using `awk '{print $1}'` to compare cleanly 
(avoiding filename differences confusing the diff output).

Result of `diff hashes_before.txt hashes_after.txt` → **empty output** 
→ hashes are identical → **data integrity confirmed after copy** ✅

## Silent Data Corruption Simulation
Injected 7 bytes ("CORRUPT") at byte position 1024 using:
```bash
printf 'CORRUPT' | sudo dd of=/teststorage/s04_testfile_copy bs=1 seek=1024 conv=notrunc
```
This simulates silent data corruption — file size stays the same, 
only 7 bytes out of 52,428,800 bytes changed.

## Corruption Detection Result
MD5 hash after corruption: 9e7b63cc2a4d3a0d23334c6b605f9f09
Original MD5 hash: 25e317773f308e446cc84c503a6d1f85

`diff hashes_before.txt hashes_corrupted.txt` → showed clear differences
→ **corruption successfully detected** ✅

## Key Learning
Checksums are extremely sensitive — even a 7-byte change in a 50MB file 
produces a completely different hash. This is why checksum verification 
is the gold standard for data integrity validation in storage testing.
Always compare only hash values (not full checksum output lines) to avoid 
false positives from filename differences.
