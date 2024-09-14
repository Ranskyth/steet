sudo git clone https://github.com/m4ll0k/SecretFinder.git
sudo cd SecretFinder
sudo python3 -m pip install -r requirements.txt
sudo go install github.com/tomnomnom/waybackurls@latest
sudo go install -v github.com/tomnomnom/anew@latest
sudo go install github.com/lc/gau/v2/cmd/gau@latest
sudo go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
sudo go install github.com/tomnomnom/assetfinder@latest
sudo go install github.com/projectdiscovery/katana/cmd/katana@latest
sudo go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
sudo chmod +x hackertarget
sudo mv SecretFinder /usr/local/bin
sudo mv /root/go/bin/assetfinder /usr/local/bin
sudo mv /root/go/bin/gau /usr/local/bin
sudo mv /root/go/bin/katana /usr/local/bin
sudo mv /root/go/bin/subfinder /usr/local/bin
sudo mv /root/go/bin/waybackurls /usr/local/bin
sudo mv /root/go/bin/anew /usr/local/bin
sudo mv /root/go/bin/httpx /usr/local/bin
sudo mv ./hackertarget /usr/local/bin
sudo mv steet /usr/local/bin
