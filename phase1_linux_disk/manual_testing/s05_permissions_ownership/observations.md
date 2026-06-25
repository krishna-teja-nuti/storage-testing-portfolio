# S05 — File Permissions & Ownership Testing — Observations

## Permissions Testing (chmod)

### chmod 777 — Full Permissions
Set `rwxrwxrwx` — all users (owner, group, others) have read, write, execute.
Verified via `ls -la` — permissions column shows `-rwxrwxrwx`.

### chmod 400 — Read Only for Owner
Set `r--------` — only owner can read, no write/execute for anyone.
Verified negative test — attempting to write as non-root user produced:
`Permission denied` error — confirming restrictive permissions work correctly.

## Ownership Testing (chown)
Changed ownership from `root:root` to `teja4b5:teja4b5` using `chown`.
Verified via `ls -la` — owner and group columns updated correctly.
File retained its permissions (644) after ownership change.

## ACL Testing (getfacl / setfacl)

### Before setfacl
Standard permissions only:
- user (teja4b5): rw-
- group: r--
- other: r--

### After setfacl -m u:root:rwx
Added explicit ACL entry for root user:
- user (teja4b5): rw- (unchanged)
- user:root: rwx (new ACL entry)
- group: r--
- other: r--
- mask: rwx

ACL allows granting specific permissions to specific users without 
modifying the standard owner/group/other permission model.

## Key Learning
Standard Linux permissions (chmod/chown) control access at owner/group/other 
level. ACLs (setfacl/getfacl) provide fine-grained control for individual 
users or groups — essential for NFS environments where multiple users need 
different access levels on the same files.
