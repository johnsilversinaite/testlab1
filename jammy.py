import os
os.system('curl -skLo gdown https://raw.githubusercontent.com/kmille36/GoogleDriveCurl/main/gdown && chmod +x gdown')
os.system('bash gdown jammy.tar 1-Rw75HWYHdlfRgYTvfll43eNmXPrguWX && tar -xf jammy.tar')
os.system('rm -rf jammy.tar')
os.system('cd jammy && curl -LO https://proot.gitlab.io/proot/bin/proot && chmod +x proot')
os.system('cd jammy && ./proot -S . apt-get update')
os.system('cd jammy && ./proot -S . apt-get -y full-upgrade')
os.system('cd jammy && ./proot -S . apt-get -y dist-upgrade')
os.system('cd jammy && ./proot -S . apt-get -y autoremove')
os.system('cd jammy && ./proot -S . apt-get install -y wget curl nano xz-utils')
os.system('cd jammy && ./proot -S . bash -c "wget https://github.com/tmate-io/tmate/releases/download/2.4.0/tmate-2.4.0-static-linux-amd64.tar.xz && tar -xvf tmate-2.4.0-static-linux-amd64.tar.xz && rm -rf tmate-2.4.0-static-linux-amd64.tar.xz && mv tmate-2.4.0-static-linux-amd64/tmate tmate && rm -rf tmate-2.4.0-static-linux-amd64 && chmod +x tmate"')
os.system('cd jammy && ./proot -S . ./tmate -F')