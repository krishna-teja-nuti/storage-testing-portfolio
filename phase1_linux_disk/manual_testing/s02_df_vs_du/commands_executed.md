# S02 — Commands Executed

## 1. Check filesystem level usage
```bash
df -h /teststorage
```
Shows total, used, and available space at the filesystem level.

## 2. Check directory level usage
```bash
du -sh /teststorage
```
Shows actual space consumed by visible files/directories.

## 3. Create test file held open by a process
```bash
sudo dd if=/dev/zero of=/teststorage/openfile.dat bs=1M count=500
sudo tail -f /teststorage/openfile.dat &
```
Creates a 500MB file and opens it in the background, keeping a file descriptor active.

## 4. Delete the file while still open
```bash
sudo rm /teststorage/openfile.dat
```
Removes the file from the directory listing, but the open file descriptor keeps it on disk.

## 5. Identify the process holding the deleted file
```bash
sudo lsof 2>/dev/null | grep deleted | grep openfile
```
Lists open file descriptors pointing to deleted files, filtered for our test file.

## 6. Free space safely without killing the process
```bash
sudo bash -c "> /proc/<PID>/fd/<FD>"
```
Truncates the file descriptor's contents to zero, freeing disk space immediately.

## 7. Clean up
```bash
sudo kill <PID>
```
Terminates the test process after verification.
