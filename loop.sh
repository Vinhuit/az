pip3 install pexpect --user
export resource=$(az resource list  | jq -r 'first(.[].resourceGroup)')
export myip=$(az vm create --name $RANDOM --resource-group $resource --image UbuntuLTS --size Standard_DS3_v2 --location southeastasia --admin-username caubequay00 --admin-password Qwertyuiop12@# | echo $(jq -r 'first(.publicIpAddress)'))
python nim.py $myip $1
rm ~/.ssh/known_hosts 
sleep 2
for run in {1..20}
do
  bash skydevice_conly.sh $1 &
  sleep 2
done
