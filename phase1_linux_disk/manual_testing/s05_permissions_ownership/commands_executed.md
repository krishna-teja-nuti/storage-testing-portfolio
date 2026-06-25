# S05 — Commands Executed

## 1. Create test file
```bash
sudo touch /teststorage/test_permissions.txt
```
Creates an empty test file owned by root for permission testing.

## 2. Set full permissions (chmod 777)
```bash
sudo chmod 777 /teststorage/test_permissions.txt
ls -la /teststorage/test_permissions.txt
```
Sets read, write, execute for owner, group, and others.
`777` in octal = `rwxrwxrwx` in symbolic notation.

## 3. Set restrictive permissions (chmod 400)
```bash
sudo chmod 400 /teststorage/test_permissions.txt
ls -la /teststorage/test_permissions.txt
```
Sets read-only for owner, no permissions for group or others.
`400` in octal = `r--------` in symbolic notation.

## 4. Negative test — access denied
```bash
bash -c 'echo "test" >> /teststorage/test_permissions.txt' 2> access_denied_output.txt
```
Attempts to write to a read-only file as non-root user.
Expected result: `Permission denied` error captured in output file.

## 5. Change ownership (chown)
```bash
sudo chmod 644 /teststorage/test_permissions.txt
sudo chown teja4b5:teja4b5 /teststorage/test_permissions.txt
ls -la /teststorage/test_permissions.txt
```
Restores file to readable state (644) then changes ownership from 
root:root to teja4b5:teja4b5. Format: `chown user:group file`.

## 6. Check ACL before changes (getfacl)
```bash
getfacl /teststorage/test_permissions.txt
```
Displays current Access Control List entries for the file.
Shows standard permissions in ACL format (user/group/other).

## 7. Add ACL entry (setfacl)
```bash
sudo setfacl -m u:root:rwx /teststorage/test_permissions.txt
getfacl /teststorage/test_permissions.txt
```
`-m` flag modifies ACL. `u:root:rwx` adds rwx permissions for root user 
specifically, without changing the standard owner/group/other permissions.
