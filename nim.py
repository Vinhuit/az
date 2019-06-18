from pexpect import pxssh
import sys
try:
    s = pxssh.pxssh(options={
                    "StrictHostKeyChecking": "no",
                    "UserKnownHostsFile": "/dev/null"})
    hostname = sys.argv[1]
    username = 'caubequay00'
    password = 'Qwertyuiop12@#'
    s.login(hostname, username, password)
    s.sendline('uptime')   # run a command
    s.prompt()             # match the prompt
    print(s.before)        # print everything before the prompt.
    s.sendline('screen -S "myscreen" -d -m')
    s.prompt()
    s.sendline('sleep 1')
    s.prompt()
    s.sendline('screen -r "myscreen" -X stuff $"wget https://raw.githubusercontent.com/Vinhuit/azurenimpool/master/azure_script/run_3.sh;chmod 777 run_3.sh;./run_3.sh\n"')
    s.prompt()
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
