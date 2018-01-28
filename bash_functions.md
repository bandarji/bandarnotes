# Bash Functions and One-liners

## Git

### Move to Git Repository Root Directory

```bash
function git_top() {
  tmp_pwd="$(pwd)"
  i=0
  while ! [ -d .git  -o ${i} -gt 30 ]; do
    i=$((i+1))
    cd ../
  done
  OLDPWD="${tmp_pwd}"
}
```

## Retrieve Specific Pull Request

```bash
function git_pr() {
  [[ -z ${1} ]] \
    && { echo "Supply pull request number"; return 1; } \
    || { git fetch origin pull/${1}/head:pr_${1}; git checkout pr_${1}; }
}
```

## Regular Expressions

```bash
alias reg_mac='echo [0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}'
alias grep_mac="grep -E $(reg_mac)"
alias reg_email='echo "[^[:space:]]+@[^[:space:]]+"'
alias reg_ip='echo "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"'
```

## Syntax Checkers

```bash
alias chk_yaml='python -c "import sys, yaml as y; y.safe_load(open(sys.argv[1]))"'
alias chk_json='jq "." >/dev/null <'
alias chk_puppet='puppet parser validate'
```

## Systems Administration

### Hardware Information

```bash
system_profiler
dmidecode
```

### Useful `cat` and `grep`

```bash
cat -v # show non-printing, invisible
cat -e # show line ends ($) and non printing
cat -t # show tabs (^I) and non-printing
cat -s # squeeze repeat blank lines into one blank line
cat -n # number lines
cat -b # number non-blank lines
#
grep -h # show only matches, not filenames
grep -l # show all matching filenames
grep -L # show all non-matching filenames
grep -m NUM # stop grep after NUM matches
```

### Various

```bash
# shell parameter expansion - variable substitution
${variable:-word} # If variable is unset or null, the expansion of word is substituted. Otherwise, the value of parameter is substituted.
${variable:=word} # If variable is unset or null, the expansion of word is assigned to parameter. The value of parameter is then substituted. Positional parameters and special parameters may not be assigned to in this way.
${variable:?word} # If variable is null or unset, the expansion of word is written to the standard error and the shell, if it is not interactive, exits. Otherwise, the value of parameter is substituted.
${variable:+word} # If variable is null or unset, nothing is substituted, otherwise the expansion of word is substituted.

${variable:offset}
${variable:offset:length} # Expands to up to length characters of parameter starting at the character specified by offset. If length is omitted, expands to the substring of parameter starting at the character specified by offset. length and offset are arithmetic expressions (see Shell Arithmetic). This is referred to as Substring Expansion.

${!prefix*}
${!prefix@} # Expands to the names of variables whose names begin with prefix, separated by the first character of the IFS special variable. When ‘@’ is used and the expansion appears within double quotes, each variable name expands to a separate word.

${!name[@]}
${!name[*]} # If name is an array variable, expands to the list of array indices (keys) assigned in name. If name is not an array, expands to 0 if name is set and null otherwise. When ‘@’ is used and the expansion appears within double quotes, each key expands to a separate word.
${#parameter} # The length in characters of the expanded value of parameter is substituted. If variable is ‘*’ or ‘@’, the value substituted is the number of positional parameters. If variable is an array name subscripted by ‘*’ or ‘@’, the value substituted is the number of elements in the array.


# substring removal
a="aacdff"
${variable#word} # remove from beginning, shortest
echo ${a#*a} # acdff
${variable##word} # remove from beginning, longest
echo ${a##*a} # cdff
${variable%word} # remove from end, shortest
echo ${a%f*} # aacdf
${variable%%word}  # remove from end, longest
echo ${a%%f*} # aacd

${variable/pattern/string} # Parameter is expanded and the longest match of pattern against its value is replaced with string. If pattern begins with ‘/’, all matches of pattern are replaced with string. Normally only the first match is replaced. If pattern begins with ‘#’, it must match at the beginning of the expanded value of parameter. If pattern begins with ‘%’, it must match at the end of the expanded value of parameter. If string is null, matches of pattern are deleted and the / following pattern may be omitted. If variable is ‘@’ or ‘*’, the substitution operation is applied to each positional parameter in turn, and the expansion is the resultant list. If variable is an array variable subscripted with ‘@’ or ‘*’, the substitution operation is applied to each member of the array in turn, and the expansion is the resultant list.

# case modification
${PARAMETER^}
${PARAMETER^^}
${PARAMETER,}
${PARAMETER,,}
${PARAMETER~}
${PARAMETER~~} # The ^ operator modifies the first character to uppercase, the , operator to lowercase. When using the double-form (^^ and ,,), all characters are converted.

# case modification in arrays
array=(This is some Text)
echo "${array[@],}" # this is some text
echo "${array[@],,}" # this is some text
echo "${array[@]^}" # This Is Some Text
echo "${array[@]^^}" # THIS IS SOME TEXT
echo "${array[2]^^}" # TEXT

# find -printf show filename
find path/ -printf "%p\n" # show full path
find path/ -printf "%P\n" # show relative path
```
