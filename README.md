# CS179IPROJECT

SSH into Clouldlab node that will act as server:

sudo apt-get update
sudo apt install docker.io
sudo chmod 666 /var/run/docker.sock
sudo apt-get install vim
vim Dockerfile (then copy all contents of my dockerfile)
docker build -t mydocker .
docker run -ti -p 8080:8080 mydocker
cd ../..
cd opt
cd caffe
cd build
cmake ..
make all
make install
make runtest
cd ../../..
cd workspace 
git clone --recursive https://github.com/fabiocarrara/deep-parking.git
cd deep-parking
wget http://cnrpark.it/models/CNRPark+EXT_Trained_Models_mAlexNet.zip
sudo apt-get install unzip
unzip CNRPark+EXT_Trained_Models_mAlexNet.zip
