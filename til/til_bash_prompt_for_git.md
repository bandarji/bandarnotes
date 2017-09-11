# Bash Prompt For Git

Decorate your Bash prompt with useful Git status messaging. Place these
instructions within your `~/.bash_profile` file. Download git-prompt script from
[here](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh).

## Method For Newer Systems

```bash
if [ -f ~/.git-prompt.sh ]; then
  . ~/.git-prompt.sh
  export GIT_PS1_SHOWDIRTYSTATE=true
  export GIT_PS1_SHOWCOLORHINTS=true
  export GIT_PS1_UNTRACKEDFILES=true
  export PROMPT_COMMAND="__git_ps1 '\u@\h:\w' '\\$ '"
fi
```

## Method For Older Systems

```bash
function git_in_dir_tree() {
  git rev-parse --is-inside-work-tree >/dev/null 2>&1
}

function git_prompt_older() {
  local txtbld=$(tput bold)             # Bold
  local bldred=${txtbld}$(tput setaf 1) #  red
  local bldblu=${txtbld}$(tput setaf 4) #  blue
  local bldwht=${txtbld}$(tput setaf 7) #  white
  local bldcyn=${txtbld}$(tput setaf 9) #  cyan
  local txtrst=$(tput sgr0)             # Reset
  if git_in_dir_tree ; then
    local git_args="rev-parse --symbolic-full-name --abbrev-ref HEAD"
    local git_branch="$(git ${git_args} 2>/dev/null)"
    printf "${bldcyn}${git_branch}"
    local git_status="$(git status --short 2>/dev/null)"
    [[ "${#git_status}" -lt 1 ]] \
      && printf "${bldred} - ${bldcyn}" \
      || printf "${bldblu} + ${bldcyn}"
    [[ "${git_branch}" == "HEAD" ]] \
      && printf "@%s%s " "$(git name-rev --name-only HEAD)" "${txtrst}" \
      || printf "@%s%s " "$(git rev-parse --short HEAD)" "${txtrst}"
  fi
}

export -f git_in_dir_tree git_prompt_older
export PROMPT_COMMAND="git_prompt_older"
```
