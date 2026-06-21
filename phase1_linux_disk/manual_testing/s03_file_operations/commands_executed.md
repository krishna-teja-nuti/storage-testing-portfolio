# S03 — Commands Executed

## 1. Create a file of specific size
```bash
dd if=/dev/zero of=/teststorage/file_100mb bs=1M count=100
```
`dd` reads from `/dev/zero` (an infinite source of null bytes) and writes to the 
target file. `bs=1M` sets the block size to 1 megabyte per write operation, and 
`count=100` repeats it 100 times — producing an exact 100MB file. This is the 
standard way to create test files of a precise, known size for storage testing.

## 2. Check file metadata
```bash
stat /teststorage/file_100mb
```
`stat` displays detailed filesystem metadata for a file — exact byte size, number 
of disk blocks allocated, inode number, permissions, and all four timestamps 
(access, modify, change, birth). This is used to verify a file's true on-disk 
footprint, not just its apparent size.

## 3. Copy file
```bash
cp /teststorage/file_100mb /teststorage/file_100mb_copy
```
`cp` creates a full, independent duplicate of the file — a new inode is allocated 
and the entire 100MB of data is physically read and rewritten. After this 
operation, both files exist simultaneously and consume disk space separately.

## 4. Move file
```bash
mv /teststorage/file_100mb /teststorage/file_100mb_moved
```
`mv` relocates or renames a file. Within the same filesystem, this is a fast 
metadata-only operation (no actual data is copied) — it simply updates the 
directory entry to point to a new name. Total disk usage remains unchanged 
since the original is removed in the same operation.

## 5. Sync copy with rsync
```bash
rsync -avh /teststorage/file_100mb_moved /teststorage/file_100mb_rsync
```
`rsync` synchronizes files between locations, similar to `cp` but with built-in 
progress reporting and the ability to only transfer changed data on subsequent 
runs. The `-a` flag preserves permissions/timestamps (archive mode), `-v` shows 
verbose output, and `-h` formats sizes in human-readable form (e.g., "100M" 
instead of raw bytes).

## 6. Test filesystem full behavior
```bash
sudo dd if=/dev/zero of=/teststorage/bigfile bs=1M
echo "test" > /teststorage/testfile.txt
```
The first command writes continuously until the filesystem runs completely out 
of space, triggering an `IO error: No space left on device`. The second command 
then attempts a separate, unrelated write to confirm the filesystem rejects ALL 
new writes — not just the one that caused the original failure — proving the 
filesystem is genuinely at 100% capacity.

## 7. Create sparse file
```bash
dd if=/dev/zero of=/teststorage/sparse_file bs=1M count=0 seek=1000
ls -lh /teststorage/sparse_file
du -sh /teststorage/sparse_file
```
`seek=1000` moves the write pointer 1000MB into the file before writing, while 
`count=0` means zero actual blocks are written. This creates a "sparse" file — 
the filesystem records a 1000MB apparent size (`ls -lh`) but allocates no real 
disk blocks for the empty region (`du -sh` shows 0). Useful for understanding 
how sparse files can cause apparent vs actual size discrepancies.
