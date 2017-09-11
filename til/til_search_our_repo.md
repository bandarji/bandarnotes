# Search Our Git Repository

## Problem

You need to find references to something specific in a Git repository.

## Solution

```
grep -i -r ${LOOKING_FOR} * | awk -F: '{ print $1 }' | uniq
```

## Example

I want to find tickets and other text containing the string 'tor507'.

```
sje@bandarbox:~/src/arepo (master)$ grep -i -r tor507 * | awk -F: '{ print $1 }' | uniq
bob/TECHOPS-10051
bob/TECHOPS-11071
bob/TECHOPS-12137
lisa/work/TECHOPS-12083
sje/src/network_gear.yaml
sje/src/switch_port_report.py
wiki/maintcal.md
wiki/meetings/20171003.md
wiki/all_projects.md
```

## Even Better (Than the Real Thing)

Add this Bash function to your `~/.bash_profile`:

```bash
function gitgrep() {
    # Displays files containing references to string supplied as argument
    # Does nothing if nothing passed to the function
    [[ -z ${1} ]] || grep -i -r ${1} * | awk -F: '{ print $1 }' | uniq
}
```
