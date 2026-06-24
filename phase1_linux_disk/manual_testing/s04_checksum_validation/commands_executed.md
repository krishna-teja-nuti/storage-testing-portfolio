# S04 — Commands Executed

## 1. Create test file
```bash
dd if=/dev/zero of=/teststorage/s04_testfile bs=1M count=50
```
Creates a 50MB file filled with zero bytes — consistent, reproducible 
test data for checksum verification.

## 2. Generate checksums before operation
```bash
md5sum /teststorage/s04_testfile > checksums_before.txt
sha256sum /teststorage/s04_testfile >> checksums_before.txt
sha512sum /teststorage/s04_testfile >> checksums_before.txt
```
Generates three checksums (MD5, SHA256, SHA512) and saves them to a file 
before any file operation. MD5 is fast but weaker; SHA256 and SHA512 are 
cryptographically stronger and preferred for integrity verification.

## 3. Copy file and generate checksums after
```bash
cp /teststorage/s04_testfile /teststorage/s04_testfile_copy
md5sum /teststorage/s04_testfile_copy > checksums_after.txt
sha256sum /teststorage/s04_testfile_copy >> checksums_after.txt
sha512sum /teststorage/s04_testfile_copy >> checksums_after.txt
```
Copies the file and immediately regenerates checksums on the destination 
to verify no data loss occurred during copy.

## 4. Extract and compare hash values only
```bash
awk '{print $1}' checksums_before.txt > hashes_before.txt
awk '{print $1}' checksums_after.txt > hashes_after.txt
diff hashes_before.txt hashes_after.txt > hash_diff_output.txt
```
`awk '{print $1}'` extracts only the hash value (first column), ignoring 
the filename. This avoids false positives from filename differences when 
comparing checksums of source and destination files.
Empty `diff` output = hashes match = integrity confirmed.

## 5. Simulate silent data corruption
```bash
printf 'CORRUPT' | sudo dd of=/teststorage/s04_testfile_copy bs=1 seek=1024 conv=notrunc
```
Injects 7 bytes at byte position 1024 without truncating the file. 
`conv=notrunc` ensures the rest of the file is untouched — simulating 
real silent corruption where file size appears normal but content is altered.

## 6. Detect corruption via checksum
```bash
md5sum /teststorage/s04_testfile_copy > checksums_corrupted.txt
awk '{print $1}' checksums_corrupted.txt > hashes_corrupted.txt
diff hashes_before.txt hashes_corrupted.txt > corruption_detected.txt
```
Regenerates checksum after corruption and compares against original. 
Non-empty `diff` output confirms corruption was detected.
