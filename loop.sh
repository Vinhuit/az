pip3 install pexpect --user
for run in {1..5}
do
  bash skydevice_conly.sh &
  sleep 30
done
