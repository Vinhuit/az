import pexpect
import sys
child = pexpect.spawn('ssh caubequay00@'+sys.argv[1]+' '+ 'mkdir aaaaaaaa')
child.expect('.*(yes/no)? ')
child.sendline('yes')
child.expect ('password: ')
child.sendline('Qwertyuiop12@#')
child.expect('.*')
child.sendline('rm -rf sky*')
child.sendline('screen -S "myscreen" -d -m')
child.sendline('sleep 1')
child.sendline('screen -r "myscreen" -X stuff $"wget https://raw.githubusercontent.com/Vinhuit/azurenimpool/master/azure_script/run3.sh;chmod 777 run3.sh;./run3.sh\n"')
child.sendline('exit')
#child.interact() 
print(str(child))



