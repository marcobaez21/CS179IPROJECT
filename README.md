# CS179IPROJECT


# SERVER INSTRUCTIONS

SSH into Clouldlab node that will act as server:

sudo apt-get update 

sudo apt install docker.io

sudo chmod 666 /var/run/docker.sock

sudo apt-get install vim

vim Dockerfile (then copy all contents of my dockerfile)

docker build -t mydocker .

docker run -it -p 8080:8080 mydocker

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

apt-get update

apt-get install unzip

unzip CNRPark+EXT_Trained_Models_mAlexNet.zip

apt-get install vim

vim server.py (and copy my server.py file)

pip install tqdm

pip install python-dateutil==2.5.0

pip install functools32

pip install --upgrade pip

pip install google

pip install protobuf

apt-get install python-tk

python server.py

# CLIENT INSTRUCTIONS

SSH into Clouldlab node that will act as client:

sudo apt-get update

sudo apt-get insall vim

pip install tqdm

vim client.py (and copy my client.py file)

python client.py 

# (Sources)
Client and Server Python files were heavily based on code given to us by our TA Aditya, our Mentor Shixiong, and this source (https://www.thepythoncode.com/article/send-receive-files-using-sockets-python)
