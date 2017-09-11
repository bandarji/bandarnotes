Bash Style Guide
================

This document pertains to Bash, however rules and stylization carry over to
many other scripting languages. Use your best judgement to produce portable,
extendable scripts.

## Table of Contents

* [Shell Files](#shell-files)
  * [When to Use](#when-to-use)
  * [File Extensions](#file-extensions)
  * [SUID and SGID](#suid-and-sgid)
* [Environment](#environment)
  * [STDOUT vs STDERR](#stdout-vs-stderr)
* [Comments](#comments)
  * [File Header](#file-header)
  * [Function Comments](#function-comments)
  * [Implementation Comments](#implementation-comments)
  * [TODO Comments](#todo-comments)
* [Formatting](#formatting)
  * [Indentation](#indentation)
  * [Line Length and Long Strings](#line-length-and-long-strings)
  * [Pipelines](#pipelines)
  * [Loops](#loops)
  * [Case statement](#case-statement)
  * [Variable Expansion](#variable-expansion)
  * [Quoting](#quoting)
* [Features and Bugs](#features-and-bugs)
  * [Command Substitution](#command-substitution)
  * [Test](#test)
  * [Testing Strings](#testing-strings)
  * [Wildcard Expansion of Filenames](#wildcard-expansion-of-filenames)
  * [Eval](#eval)
  * [Pipes to While](#pipes-to-while)
* [Naming Conventions](#naming-conventions)
  * [Function Names](#function-names)
  * [Variable Names](#variable-names)
  * [Constants and Environment Variable Names](#constants-and-environment-variable-names)
  * [Source Filenames](#source-filenames)
  * [Read-only Variables](#read-only-variables)
  * [Local Variables](#local-variables)
  * [Function Location](#function-location)
  * [main Function](#main-function)
* [Calling Commands](#calling-commands)
  * [Checking Return Values](#checking-return-values)
  * [Builtin Commands vs External Commands](#builtin-commands-vs-external-commands)
  * [Math](#math)
  * [Useless Use of Cat](#useless-use-of-cat)


## Shell Files

### When to Use

Executables must start with `#!/bin/bash` and a minimum number of flags. Use set
to configure shell options so that calling your script as `bash <script_name>`
does not break its functionality.

Restricting all executable shell scripts to bash gives us a consistent shell
language that's installed on all our machines. Shell should only be used for
small utilities or simple wrapper scripts. While shell scripting isn't a
development language, it is used for writing various utility scripts.

### File Extensions

Executables should have no extension (strongly preferred) or a `.sh` extension.
Libraries must have a `.sh` extension and should not be executable. It is not
necessary to know what language a program is written in when executing it and
shell doesn't require an extension so we prefer not to use one for executables.

However, for libraries it's important to know what language it is and sometimes
there's a need to have similar libraries in different languages. This allows
library files with identical purposes but different languages to be identically
named except for the language-specific suffix.

### SUID and SGID

There are too many security issues with shell that make it nearly impossible to
secure sufficiently to allow SUID/SGID. While bash does make it difficult to run
SUID, it's still possible on some platforms which is why we're being explicit
about banning it.

Use sudo to provide elevated access if you need it. Avoid SUID/SGID.

## Environment

### STDOUT vs STDERR

All error messages should go to STDERR. This makes it easier to separate normal
status from actual issues. A function to print out error messages along with
other status information is recommended.

```bash
    err() {
      echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2
    }

    if ! do_something; then
      err "Unable to do_something"
      exit "${E_DID_NOTHING}"
    fi
```

## Comments

### File Header

Start each file with a description of its contents. Every file must have a
top-level comment including a brief overview of its contents. Additional script
information should also reside in this header, rather than elsewhere in the
file.

Example:

```bash
    #!/bin/bash
    #
    # Gather RRD files for combination traffic graphs
    # Maintainer: Sean Jain Ellis <sellis@marketo.com>
    #
```

### Function Comments

Any function that is not both obvious and short must be commented. Any function
in a library must be commented regardless of length or complexity. It should be
possible for someone else to learn how to use your program or to use a function
in your library by reading the comments (and self-help, if provided) without
reading the code.

All function comments should contain:

* Description of the function
* Global variables used and modified
* Arguments taken
* Returned values other than the default exit status of the last command run

Example:

```bash
    # build_graphs()
    # description: write Internet usage PNGs from collected RRD files
    # globals: none
    # arguments: none
    # returns: graphs written -- 0 == no, 1 == yes
    function build_graphs() {
      local rrd_c1="800080"
      local rrd_c2="008000"
      local rrd_c3="000080"
      local rrd_c4="FFD700"
      local rrd_gw="850"
      local rrd_gh="350"
      local rrd_args="-w ${rrd_gw} -h ${rrd_gh} -a PNG --step 60 --end now"
      rrdargs="${rrd_args} --font DEFAULT:6: --watermark $(date +%F-%R-%Z)"
```

### Implementation Comments

Comment tricky, non-obvious, interesting or important parts of your code.
This follows general coding comment practice. Don't comment everything. If
there's a complex algorithm or you're doing something out of the ordinary, put
a short comment in.

### TODO Comments

Use TODO comments for code that is temporary, a short-term solution, or
good-enough but not perfect. TODOs should include the string TODO in capital
letters, followed by your username in parentheses. A colon is optional. It's
preferable to put a bug/ticket number next to the TODO item as well.

Example:

```bash
    # TODO(sellis): Check if NFS filesystem mounted before write (OPS-00000)
```

## Formatting

While you should follow the style that's already there for files that you're
modifying, the following are required for any new code.

### Indentation

Indent 2 spaces. Do not use tabs. Use blank lines between blocks to improve
readability. Indentation is two spaces. Whatever you do, don't use tabs. For
existing files, stay faithful to the existing indentation. Again, two spaces, no
tabs. Did I mention no tabs?

### Line Length and Long Strings

Maximum line length is 80 characters. If you have to write strings that are
longer than 80 characters, this should be done with a here document or an
embedded newline if possible. Literal strings that have to be longer than 80
chars and can't sensibly be split are okay, but it's strongly preferred to find
a way to make them shorter.

```bash
    cat <<END;
    I am an exceptionally long
    string.
    END

    long_string="I am an exceptionally
      long string."
```

### Pipelines

Pipelines should be split one per line if they don't all fit on one line. If a
pipeline all fits on one line, it should be on one line.

If not, it should be split at one pipe segment per line with the pipe on the
newline and a 2 space indent for the next section of the pipe. This applies to
a chain of commands combined using `'|'` as well as to logical compounds using
`'||'` and `'&&'`.

```bash
    # All fits on one line
    command1 | command2

    # Long commands
    command1 \
      | command2 \
      | command3 \
      | command4
```

### Loops

Put `; do` and `; then` on the same line as the `while`, `for` or `if`. Loops
in shell are a bit different, but we follow the same principles as with braces
when declaring functions. That is: `; then` and `; do` should be on the same
line as the if/for/while. `else` should be on its own line and closing
statements should be on their own line vertically aligned with the opening
statement.

Example:

```bash
    for dir in ${dirs_to_cleanup}; do
      if [[ -d "${dir}/${ORACLE_SID}" ]]; then
        log_date "Cleaning up old files in ${dir}/${ORACLE_SID}"
        rm "${dir}/${ORACLE_SID}/"*
        if [[ "$?" -ne 0 ]]; then
          error_message
        fi
      else
        mkdir -p "${dir}/${ORACLE_SID}"
        if [[ "$?" -ne 0 ]]; then
          error_message
        fi
      fi
    done
```

### Case statement

A one-line alternative needs a space after the close parenthesis of the pattern
and before the `;;`. Long or multi-command alternatives should be split over
multiple lines with the pattern, actions, and `;;` on separate lines. Matching
expressions are indented one level from the `case` and `esac`. Multiline actions
are indented another level. In general, there is no need to quote match
expressions. Pattern expressions should not be preceded by an open parenthesis.
Avoid `;&` and `;;&` notations.

```bash
    case "${expression}" in
      a)
        local variable="..."
        some_command "${variable}" "${other_expr}" ...
        ;;
      absolute)
        local actions="relative"
        another_command "${actions}" "${other_expr}" ...
        ;;
      *)
        error "Unexpected expression '${expression}'"
        ;;
    esac
```

Simple commands may be put on the same line as the pattern and `;;` as long as
the expression remains readable. This is often appropriate for single-letter
option processing. When the actions don't fit on a single line, put the pattern
on a line on its own, then the actions, then ;; also on a line of its own. When
on the same line as the actions, use a space after the close parenthesis of the
pattern and another before the `;;`.

```bash
    local verbose='false'
    local aflag=''
    local bflag=''
    local files=''
    while getopts 'abf:v' flag; do
      case "${flag}" in
        a) local aflag='true' ;;
        b) local bflag='true' ;;
        f) local files="${OPTARG}" ;;
        v) local verbose='true' ;;
        *) error "Unexpected option ${flag}" ;;
      esac
    done
```

### Variable Expansion

These are meant to be guidelines, as the topic seems too controversial for a
mandatory regulation.  They are listed in order of precedence.

1. Stay consistent with what you find for existing code.
1. Quote variables, see Quoting section below.
1. Don't brace-quote single character shell specials / positional parameters, unless strictly necessary or avoiding deep confusion.
1. Prefer brace-quoting all other variables.

```bash
    # GOOD

    # Preferred style for 'special' variables:
    echo "Positional: $1" "$5" "$3"
    echo "Specials: !=$!, -=$-, _=$_. ?=$?, #=$# *=$* @=$@ \$=$$ ..."

    # Braces necessary:
    echo "many parameters: ${10}"

    # Braces avoiding confusion:
    # Output is "a0b0c0"
    set -- a b c
    echo "${1}0${2}0${3}0"

    # Preferred style for other variables:
    echo "PATH=${PATH}, PWD=${PWD}, mine=${some_var}"
    while read f; do
      echo "file=${f}"
    done < <(ls -l /tmp)

    # BAD

    # Unquoted vars, unbraced vars, brace-quoted single letter
    # shell specials.
    echo a=$avar "b=$bvar" "PID=${$}" "${1}"

    # Confusing use: this is expanded as "${1}0${2}0${3}0",
    # not "${10}${20}${30}
    set -- a b c
    echo "$10$20$30"
```

### Quoting

Always quote strings containing variables, command substitutions, spaces or
shell meta characters, unless careful unquoted expansion is required.

Prefer quoting strings that are "words" (as opposed to command options or path
names). Never quote literal integers. Be aware of the quoting rules for pattern
matches in `[[`. Use `$@` unless you have a specific reason to use `$*`.

* 'Single' quotes indicate that no substitution is desired.
* "Double" quotes indicate that substitution is required/tolerated.

```bash
    # "quote command substitutions"
    flag="$(some_command and its args "$@" 'quoted separately')"

    # "quote variables"
    echo "${flag}"

    # "never quote literal integers"
    value=32
    # "quote command substitutions", even when you expect integers
    number="$(generate_number)"

    # "prefer quoting words", not compulsory
    readonly USE_INTEGER='true'

    # "quote shell meta characters"
    echo 'Hello stranger, and well met. Earn lots of $$$'
    echo "Process $$: Done making \$\$\$."

    # "command options or path names"
    # ($1 is assumed to contain a value here)
    grep -li Hugo /dev/null "$1"

    # Less simple examples
    # "quote variables, unless proven false": ccs might be empty
    git send-email --to "${reviewers}" ${ccs:+"--cc" "${ccs}"}

    # Positional parameter precautions: $1 might be unset
    # Single quotes leave regex as-is.
    grep -cP '([Ss]pecial|\|?characters*)$' ${1:+"$1"}

    # For passing on arguments,
    # "$@" is right almost everytime, and
    # $* is wrong almost everytime:
    #
    # * $* and $@ will split on spaces, clobbering up arguments
    #   that contain spaces and dropping empty strings;
    # * "$@" will retain arguments as-is, so no args
    #   provided will result in no args being passed on;
    #   This is in most cases what you want to use for passing
    #   on arguments.
    # * "$*" expands to one argument, with all args joined
    #   by (usually) spaces,
    #   so no args provided will result in one empty string
    #   being passed on.
    # (Consult 'man bash' for the nit-grits ;-)

    set -- 1 "2 two" "3 three tres"; echo $# ; set -- "$*"; echo "$#, $@")
    set -- 1 "2 two" "3 three tres"; echo $# ; set -- "$@"; echo "$#, $@")
```

## Features and Bugs

### Command Substitution

Use `$(command)` instead of backticks. Nested backticks require escaping the
inner ones with `\`. The `$(command)` format doesn't change when nested and is
easier to read.


```bash
    # This is preferred:
    var="$(command "$(command1)")"

    # This is not:
    var="`command \`command1\``"
```

### Test

`[[ ... ]]` is preferred over `[`, `test` and `/usr/bin/[`.

`[[ ... ]]` reduces errors as no pathname expansion or word splitting takes
place between `[[` and `]]` and `[[ ... ]]` allows for regular expression
matching where `[ ... ]` does not.

```bash
    # This ensures the string on the left is made up of characters in the
    # alnum character class followed by the string name.
    # Note that the RHS should not be quoted here.
    # For the gory details, see
    # E14 at https://tiswww.case.edu/php/chet/bash/FAQ
    if [[ "filename" =~ ^[[:alnum:]]+name ]]; then
      echo "Match"
    fi

    # This matches the exact pattern "f*" (Does not match in this case)
    if [[ "filename" == "f*" ]]; then
      echo "Match"
    fi

    # This gives a "too many arguments" error as f* is expanded to the
    # contents of the current directory
    if [ "filename" == f* ]; then
      echo "Match"
    fi
```

### Testing Strings

Use quotes rather than filler characters where possible. Bash is smart enough to
deal with an empty string in a test. So, given that the code is much easier to
read, use tests for empty/non-empty strings or empty strings rather than filler
characters.

```bash
    # Do this:
    if [[ "${my_var}" = "some_string" ]]; then
      do_something
    fi

    # -z (string length is zero) and -n (string length is not zero) are
    # preferred over testing for an empty string
    if [[ -z "${my_var}" ]]; then
      do_something
    fi

    # This is OK (ensure quotes on the empty side), but not preferred:
    if [[ "${my_var}" = "" ]]; then
      do_something
    fi

    # Not this:
    if [[ "${my_var}X" = "some_stringX" ]]; then
      do_something
    fi
    To avoid confusion about what you're testing for, explicitly use -z or -n.

    # Use this
    if [[ -n "${my_var}" ]]; then
      do_something
    fi

    # Instead of this as errors can occur if ${my_var} expands to a test
    # flag
    if [[ "${my_var}" ]]; then
      do_something
    fi
```

### Wildcard Expansion of Filenames

Use an explicit path when doing wildcard expansion of filenames. As filenames
can begin with a -, expand wildcards with `./*` instead of `*`.

```bash
    # Here's the contents of the directory:
    # -f  -r  somedir  somefile

    # This deletes almost everything in the directory by force
    psa@bilby$ rm -v *
    removed directory: `somedir'
    removed `somefile'

    # As opposed to:
    psa@bilby$ rm -v ./*
    removed `./-f'
    removed `./-r'
    rm: cannot remove `./somedir': Is a directory
    removed `./somefile'
```

### Eval

Avoid the evil `eval`, which munges the input when used for assignment to
variables and can set variables without making it possible to check what those
variables were.

```bash
    # What does this set?
    # Did it succeed? In part or whole?
    eval $(set_my_variables)

    # What happens if one of the returned values has a space in it?
    variable="$(eval some_function)"
```

### Pipes to While

Use process substitution or for loops in preference to piping to while.
Variables modified in a while loop do not propagate to the parent because the
loop's commands run in a subshell. The implicit subshell in a pipe to while can
make it difficult to track down bugs.

```bash
    last_line='NULL'
    your_command | while read line; do
      last_line="${line}"
    done

    # This will output 'NULL'
    echo "${last_line}"
```

Use a for loop if you are confident that the input will not contain spaces or
special characters (usually, this means not user input).

```bash
    total=0
    # Only do this if there are no spaces in return values.
    for value in $(command); do
      total+="${value}"
    done
```

Using process substitution allows redirecting output but puts the commands in an
explicit subshell rather than the implicit subshell that bash creates for the
while loop.

```bash
    total=0
    last_file=
    while read count filename; do
      total+="${count}"
      last_file="${filename}"
    done < <(your_command | uniq -c)

    # This will output the second field of the last line of output from
    # the command.
    echo "Total = ${total}"
    echo "Last one = ${last_file}"
```

Use while loops where it is not necessary to pass complex results to the parent
shell. This is typically where some more complex "parsing" is required. Beware
that simple examples are probably more easily done with a tool such as awk. This
may also be useful where you specifically don't want to change the parent scope
variables.

```bash
    # Trivial implementation of awk expression:
    #   awk '$3 == "nfs" { print $2 " maps to " $1 }' /proc/mounts
    cat /proc/mounts | while read src dest type opts rest; do
      if [[ ${type} == "nfs" ]]; then
        echo "NFS ${dest} maps to ${src}"
      fi
    done
```

## Naming Conventions

### Function Names

Lower-case, with underscores to separate words. Separate libraries with `::`.
Parentheses are required after the function name. The keyword function is
optional, but must be used consistently throughout a project. If you're writing
single functions, use lowercase and separate words with underscore. If you're
writing a package, separate package names with `::`. Braces must be on the same
line as the function name and no space between the function name and the
parenthesis.

```bash
    # Single function
    function my_func() {
      ...
    }

    # Part of a package
    mypackage::my_func() {
      ...
    }
```

The function keyword is extraneous when `()` is present after the function name,
but enhances quick identification of functions. Also, `grep` works well against
a file to list functions.

### Variable Names

Variables names for loops should be similarly named for any variable you're
looping through.

```bash
    for zone in ${zones}; do
      something_with "${zone}"
    done
```

### Constants and Environment Variable Names

All caps, separated with underscores, declared at the top of the file. Constants
and anything exported to the environment should be capitalized.

```bash
    # Constant
    readonly PATH_TO_FILES='/some/path'

    # Both constant and environment
    declare -xr ORACLE_SID='PROD'
```

Some things become constant at their first setting (for example, via getopts).
Thus, it's okay to set a constant in getopts or based on a condition, but it
should be made readonly immediately afterwards. Note that declare doesn't
operate on global variables within functions, so readonly or export is
recommended instead.

```bash
    VERBOSE='false'
    while getopts 'v' flag; do
      case "${flag}" in
        v) VERBOSE='true' ;;
      esac
    done
    readonly VERBOSE
```

### Source Filenames

Lowercase, with underscores to separate words if desired. This is for
consistency with other code styles: `maketemplate` or `make_template`, but not
`make-template`.

### Read-only Variables

Use `readonly` or `declare -r` to ensure they're read only. As globals are
widely used in shell, it's important to catch errors when working with them.
When you declare a variable that is meant to be read-only, make this explicit.

```bash
    zip_version="$(dpkg --status zip | grep Version: | cut -d ' ' -f 2)"
    if [[ -z "${zip_version}" ]]; then
      error_message
    else
      readonly zip_version
    fi
```

### Local Variables

Declare function-specific variables with local. Declaration and assignment
should be on different lines. Ensure that local variables are only seen inside a
function and its children by using local when declaring them. This avoids
polluting the global name space and inadvertently setting variables that may
have significance outside the function.

Declaration and assignment must be separate statements when the assignment value
is provided by a command substitution; as the 'local' builtin does not propagate
the exit code from the command substitution.

```bash
    my_func2() {
      local name="$1"

      # Separate lines for declaration and assignment:
      local my_var
      my_var="$(my_func)" || return

      # DO NOT do this: $? contains the exit code of 'local', not my_func
      local my_var="$(my_func)"
      [[ $? -eq 0 ]] || return

      ...
    }
```

### Function Location

Put all functions together in the file just below constants. Don't hide
executable code between functions. If you've got functions, put them together
near the top of the file. Only includes, set statements and setting constants
may be done before declaring functions.

Don't hide executable code between functions. Doing so makes the code difficult
to follow and results in nasty surprises when debugging.

### main Function

A function called `main` is required for scripts long enough to contain at least
one other function. In order to easily find the start of the program, put the
main program in a function called main as the bottom most function. This
provides consistency with the rest of the code base as well as allowing you to
define more variables as local (which can't be done if the main code is not a
function). The last non-comment line in the file should be a call to main:

```bash
    main "${@}"
```

## Calling Commands

### Checking Return Values

Always check return values and give informative return values. For unpiped
commands, use `$?` or check directly via an `if` statement to keep it simple.

```bash
    if ! mv "${file_list}" "${dest_dir}/" ; then
      echo "Unable to move ${file_list} to ${dest_dir}" >&2
      exit "${E_BAD_MOVE}"
    fi

    # Or
    mv "${file_list}" "${dest_dir}/"
    if [[ "$?" -ne 0 ]]; then
      echo "Unable to move ${file_list} to ${dest_dir}" >&2
      exit "${E_BAD_MOVE}"
    fi
```

Bash also has the `PIPESTATUS` variable that allows checking of the return code
from all parts of a pipe. If it's only necessary to check success or failure of
the whole pipe, then the following is acceptable:

```bash
    tar -cf - ./* | ( cd "${dir}" && tar -xf - )
    if [[ "${PIPESTATUS[0]}" -ne 0 || "${PIPESTATUS[1]}" -ne 0 ]]; then
      echo "Unable to tar files to ${dir}" >&2
    fi
```

However, as `PIPESTATUS` will be overwritten as soon as you do any other
command, if you need to act differently on errors based on where it happened in
the pipe, you'll need to assign `PIPESTATUS` to another variable immediately
after running the command (don't forget that `[` is a command and will wipe out
`PIPESTATUS`).

```bash
    tar -cf - ./* | ( cd "${DIR}" && tar -xf - )
    return_codes=(${PIPESTATUS[*]})
    if [[ "${return_codes[0]}" -ne 0 ]]; then
      do_something
    fi
    if [[ "${return_codes[1]}" -ne 0 ]]; then
      do_something_else
    fi
```

### Builtin Commands vs External Commands

Given the choice between invoking a shell builtin and invoking a separate
process, choose the builtin. Prefer builtins such as the Parameter
Expansion functions in `bash(1)` as more robust and portable (especially
when compared to things like `sed`).

```bash
    # Prefer this:
    addition=$((${X} + ${Y}))
    substitution="${string/#foo/bar}"

    # Instead of this:
    addition="$(expr ${X} + ${Y})"
    substitution="$(echo "${string}" | sed -e 's/^foo/bar/')"

    name='bahamas10'

    # wrong
    prog=$(basename "$0")
    nonumbers=$(echo "$name" | sed -e 's/[0-9]//g')

    # right
    prog=${0##*/}
    nonumbers=${name//[0-9]/}
```

### Math

Use `((...))` and `$((...))`.

```bash
    a=5
    b=4

    # wrong
    if [[ $a -gt $b ]]; then
        :
    fi

    # right
    if ((a > b)); then
        :
    fi
```

Do not use `let`.

### Useless Use of Cat

Avoid `cat(1)` when unneeded. This extends to piping to multiple `grep` commands
when a single execution could take care of things while remaining readable. As
a general rule, limit process ID creation, process forks and use of pipe. Don't
feed information into a script with `cat` when redirection would suffice.

```bash
# Please do not do this
cat file | grep foo

# Correct methods
grep foo < file
grep foo file

# also wrong
cat file | grep howdy | awk '{ print $4 }'

# better
awk '/howdy/ { print $4 }' file
```
