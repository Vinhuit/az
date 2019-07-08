pip3 install pexpect --user
export resource=$(az resource list  | jq -r 'first(.[].resourceGroup)')
if [ $3 -gt 499 ]; then
  url="http://xjsonserver01.herokuapp.com/temp/""$3"
else
  url="http://xjsonserver01.herokuapp.com/rerunaccount/""$3"
STATUS=$(curl -k -s -o /dev/null -w '%{http_code}' -i -H "Accept: application/json" -H "Content-Type:application/json" -X PUT --data "{\"device\":\"$2\",\"name\":\"$1\",\"isStart\":\"True\"}" "$url")
echo "Got $STATUS"
export myip=$(az vm create --name $RANDOM --resource-group $resource --image UbuntuLTS --size Standard_DS3_v2 --location southeastasia --admin-username caubequay00 --admin-password Qwertyuiop12@# | echo $(jq -r 'first(.publicIpAddress)'))
python nim.py $myip $1
rm ~/.ssh/known_hosts 
sleep 2
for run in {1..20}
do
  bash skydevice_conly.sh $1 &
  sleep 2
done
sleep 1200
