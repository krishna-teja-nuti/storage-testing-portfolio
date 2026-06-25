# Jira Ticket — S05 File Permissions & Ownership Testing

**Ticket Type:** Test Finding / Permission Verification
**Priority:** Medium
**Status:** Closed - No Action Needed

## Summary
Validated Linux file permission scenarios including chmod, chown, and ACL 
testing using setfacl/getfacl on a test file on /teststorage.

## Test Steps
1. Created test file on /teststorage
2. Applied chmod 777 — verified full permissions for all users
3. Applied chmod 400 — verified read-only for owner only
4. Negative test — attempted write on read-only file as non-root user
5. Changed ownership using chown from root:root to teja4b5:teja4b5
6. Verified ACL before setfacl using getfacl
7. Added ACL entry for root user using setfacl -m u:root:rwx
8. Verified ACL after setfacl using getfacl

## Expected Result
- chmod changes should reflect immediately in ls -la output
- Write attempt on chmod 400 file should produce Permission denied error
- chown should update owner and group without affecting permissions
- setfacl should add specific user ACL entry without modifying standard permissions

## Actual Result
- chmod 777 → -rwxrwxrwx ✅
- chmod 400 → -r-------- ✅
- Write attempt → Permission denied ✅
- chown teja4b5:teja4b5 → ownership updated correctly ✅
- setfacl → user:root:rwx added correctly, standard permissions unchanged ✅

## Observation (Notable Finding)
ACLs allow granting specific permissions to individual users beyond the 
standard owner/group/other model. This is particularly important in NFS 
environments — a common real-world storage bug involves NFS permission 
mismatches where local permissions appear correct but ACL entries cause 
unexpected access denial or permission grants for specific users.

## Evidence Attached
- chmod_777_output.txt
- chmod_400_output.txt
- access_denied_output.txt
- chown_output.txt
- getfacl_before_output.txt
- getfacl_after_output.txt

## Verdict
PASS — All permission scenarios behaved as expected. ACL functionality 
confirmed working on ext4 filesystem.
