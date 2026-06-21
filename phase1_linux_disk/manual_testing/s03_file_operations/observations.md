# S03 — File Operations & Large File Handling — Observations

## File Creation (dd)
Created a 100MB file using `dd if=/dev/zero of=file_100mb bs=1M count=100`. 
Confirmed exact byte count (104857600 bytes) in dd output.

## File Metadata (stat)
`stat` confirmed exact size, block allocation (204800 blocks), inode number, 
and full timestamp set (access/modify/change/birth).

## Copy (cp)
`cp` created an exact duplicate (`file_100mb_copy`) — same size, separate inode, 
original file untouched after copy.

## Move (mv)
`mv` relocated the file (`file_100mb` → `file_100mb_moved`) without duplicating 
data — confirmed via directory listing showing original name gone, new name present.

## Sync Copy (rsync)
`rsync -avh` copied the file with visible transfer statistics (69.92 MB/s, 
total size confirmation) — more informative than the silent `cp` command.

## Filesystem Full Behavior
Filled `/teststorage` to 100% capacity using `dd`. Observed:
- `dd` failed with: `No space left on device`
- Further write attempt (`echo > file`) also failed with the same error
- `df -h` confirmed 0 bytes available, 100% used
- Freeing space (`rm bigfile`) immediately restored availability to 9.0G

## Sparse File Behavior
Created a sparse file using `dd ... count=0 seek=1000`:
- `ls -lh` reported apparent size: 1000M
- `du -sh` reported actual disk usage: 0

Confirms sparse files only consume disk blocks for data actually written — 
directly relevant to df vs du investigation from S02.

## Key Learning
Standard file operations (dd, cp, mv, rsync) behave predictably, but boundary 
testing (filesystem full) and special file types (sparse files) are essential 
to validate since they directly affect capacity monitoring and alerting logic 
used in production storage systems.
