from pexpect import pxssh
import sys
try:
    s = pxssh.pxssh(options={
                    "StrictHostKeyChecking": "no",
                    "UserKnownHostsFile": "/dev/null"})
    hostname = sys.argv[1]
    try:
        name = sys.argv[2]
    except:
        name = "Vinh"
    
    username = 'caubequay00'
    password = 'Qwertyuiop12@#'
    s.login(hostname, username, password)
    s.sendline('uptime')   # run a command
    s.prompt()             # match the prompt
    print(s.before)        # print everything before the prompt.
    s.sendline('sudo su')
    s.set_unique_prompt()
    s.sendline('sleep 1')
    s.set_unique_prompt()
    s.sendline('screen -S "myscreen" -d -m')
    s.set_unique_prompt())
    s.sendline('sleep 1')
    s.set_unique_prompt()
    if name =="Danh":
        s.sendline('screen -r "myscreen" -X stuff $"wget https://raw.githubusercontent.com/Vinhuit/azurenimpool/master/azure_script/run_danh.sh;chmod 777 run_danh.sh;./run_danh.sh\n"')
    elif name == "Mai":
        s.sendline('screen -r "myscreen" -X stuff $"wget https://raw.githubusercontent.com/Vinhuit/azurenimpool/master/azure_script/run_mai.sh;chmod 777 run_mai.sh;./run_mai.sh\n"')
    elif name == "Hoang":
        s.sendline('screen -r "myscreen" -X stuff $"wget https://raw.githubusercontent.com/Vinhuit/azurenimpool/master/azure_script/run_hoang.sh;chmod 777 run_hoang.sh;./run_hoang.sh\n"')
    else:
        s.sendline('screen -r "myscreen" -X stuff $"wget https://raw.githubusercontent.com/Vinhuit/az/master/setupnimenv.sh;chmod 777 setupnimenv.sh;./setupnimenv.sh\n"')
    #s.sendline('screen -r "myscreen" -X stuff $"wget https://raw.githubusercontent.com/Vinhuit/azurenimpool/master/azure_script/run_3.sh;chmod 777 run_3.sh;./run_3.sh\n"')
   
    s.sendline("exit")
    s.prompt()
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
