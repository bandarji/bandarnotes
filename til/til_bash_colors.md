# Colors in Bash Output

```bash
##### reset text to normal
ResetText='\e[0m'

##### simple
Black='\e[0;30m'
Red='\e[0;31m'
Green='\e[0;32m'
Yellow='\e[0;33m'
Blue='\e[0;34m'
Purple='\e[0;35m'
Cyan='\e[0;36m'
White='\e[0;37m'

##### bold
BBlack='\e[1;30m'
BRed='\e[1;31m'
BGreen='\e[1;32m'
BYellow='\e[1;33m'
BBlue='\e[1;34m'
BPurple='\e[1;35m'
BCyan='\e[1;36m'
BWhite='\e[1;37m'

##### underlined
UBlack='\e[4;30m'
URed='\e[4;31m'
UGreen='\e[4;32m'
UYellow='\e[4;33m'
UBlue='\e[4;34m'
UPurple='\e[4;35m'
UCyan='\e[4;36m'
UWhite='\e[4;37m'

##### background
bgBlack='\e[40m'
bgRed='\e[41m'
bgGreen='\e[42m'
bgYellow='\e[43m'
bgBlue='\e[44m'
bgPurple='\e[45m'
bgCyan='\e[46m'
bgWhite='\e[47m'

##### intense
IBlack='\e[0;90m'
IRed='\e[0;91m'
IGreen='\e[0;92m'
IYellow='\e[0;93m'
IBlue='\e[0;94m'
IPurple='\e[0;95m'
ICyan='\e[0;96m'
IWhite='\e[0;97m'

##### bold-intense
BIBlack='\e[1;90m'
BIRed='\e[1;91m'
BIGreen='\e[1;92m'
BIYellow='\e[1;93m'
BIBlue='\e[1;94m'
BIPurple='\e[1;95m'
BICyan='\e[1;96m'
BIWhite='\e[1;97m'

##### intense background
bgIBlack='\e[0;100m'
bgIRed='\e[0;101m'
bgIGreen='\e[0;102m'
bgIYellow='\e[0;103m'
bgIBlue='\e[0;104m'
bgIPurple='\e[10;95m'
bgICyan='\e[0;106m'
bgIWhite='\e[0;107m'
```

## Usage

```bash
printf "${bgIBlue}${BYellow}Howdy${ResetText}\n"
```
