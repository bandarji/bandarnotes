# Bash while Loop With SSH

## The Problem

As a good sysadmin, you transition scripts and command line executions to use
while loops in place of for loops. In doing so, Secure Shell (SSH) only connects
to the first host in a supplied list of targets.

### Bad Form (Works For Short Host List)

```bash
for r_host in $(cmd_with_host_list); do
  printf "%-40s " "${r_host}"
  ssh -q ${r_host} "grep ^TCP /proc/net/sockstat" || echo "SSH FAIL"
done
```

### Good Form (Broken: Connects to Single Host)
```bash
while read r_host; do
  printf "%-40s" "${r_host}"
  ssh -q ${r_host} "grep ^TCP /proc/net/sockstat" || echo "SSH FAIL"
done < <(cmd_with_host_list)
```

## The Cause

SSH will read all STDIN, exhausting input before the next ```read``` call.

### Goodest Form

```bash
while read r_host; do
  printf "%-40s" "${r_host}"
  ssh -q ${r_host} "grep ^TCP /proc/net/sockstat" </dev/null || echo "SSH FAIL"
done < <(cmd_with_host_list)
```
