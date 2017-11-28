import os
import xml.etree.ElementTree as ET
from testLinkLibrary import *
import subprocess
import os
import datetime
import pexpect
import time
import logging
str(datetime.datetime.now())
logging.basicConfig(filename='gluster-'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.log',level=logging.DEBUG)
def creategluster():
    logging.basicConfig(filename='New.log', level=logging.DEBUG, html=True)
    gluster_creation= ["cd",
                     "sudo apt-get install -y lsb-release",
                     "sudo apt-get install -y apt-transport-https",
                     "wget -O - http://download.gluster.org/pub/gluster/glusterfs/LATEST/rsa.pub | sudo apt-key add -",
                     "echo deb https://download.gluster.org/pub/gluster/glusterfs/LATEST/Debian/$(lsb_release -sc)/apt $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/gluster.list",
                     "sudo apt-get install -y software-properties-common",
                       # sudo apt autoremove
                     "sudo add-apt-repository ppa:gluster/glusterfs-3.8",
                     "sudo apt-get update",
                     "sudo apt-get install -y glusterfs-server",
                     "sudo service glusterfs-server start"]
    # GlusterFS components use DNS for name resolutions, so configure either DNS or set up a hosts entry.
    # If you do not have a DNS on your environment, modify / etc / hosts file and update it accordingly.

    #Before proceeding to the installation, we need to configure GlusterFS repository on both storage nodes.
    # Follow the instruction to add the repository to your system.

    #Install support package for https transactions

    logging.basicConfig(level=logging.DEBUG,
                        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                        )
    for i in range(len(gluster_creation)):
        try:

            proc=subprocess.Popen([gluster_creation[i]], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            if(i==6):
                 proc.stdin.write('ivtree123\n')
	    	 print "entered password"
	    #if(proc.expect ('[pP]assword:')):
            #    proc.sendline (ivtree123)
            #expect -c spawn gluster_creation[i];expect password;send "your-password\n";interact
	    #child = pexpect.spawn(gluster_creation[i])
            #child.expect('Password:')
            #child.sendline('ivtree123')
            #print "Pexpect send the password"

            print "before wait"
            proc.wait()
            print "after wait"
            logging.debug("%s"%gluster_creation[i]+" is Executed successfully")
            output = proc.stdout.read()
           # logging.debug("process read" + output)
            print "Current command" +gluster_creation[i]+" output is\n "+ output
	    flag=True
        except  subprocess.CalledProcessError as e:
            print "Called Process Error while  executing command %s"
            flag=False
    if(flag==True):
	logging.info('successfully installed gluster here is output: '+ output)
    else:
        logging.info('Gluster installation fails')
		

def gluster_status():
    try:

        logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                            )
        proc=subprocess.Popen(['sudo service glusterfs-server status'], shell=True, stdout=subprocess.PIPE)
        print "before wait"
        proc.wait()
        print "after wait"
        output = proc.stdout.read()
        logging.debug("process read" + output)
        logging.debug("sudo service glusterfs-server status is Executed successfully")
	#logging.info('successfully shown gluster status')
	print "Current command output is" + output
        flag=True

    except subprocess.CalledProcessError as e:
        print "Called Process Error while executing command"
        flag=False
    if(flag==True):
	logging.info('Displaying current status of Gluster')
    else:
	logging.info('Command fails')

def delete_gluster():
    gluster_deletion = ["cd",
                       # "sudo apt-get --yes remove -y lsb-release",
                        "sudo apt-get remove glusterfs-server",
			"sudo apt-get remove --auto-remove glusterfs-server",
			#"sudo apt-get --yes remove -y apt-transport-https",
                        #"wget -O - http://download.gluster.org/pub/gluster/glusterfs/LATEST/rsa.pub | sudo apt-key remove -",
                        #"sudo apt autoremove"
                        #"sudo apt-get --yes remove -y glusterfs-server"
			]
    for i in range(len(gluster_deletion)):
        try:
            logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
            proc=subprocess.Popen([gluster_deletion[i]], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	    if(i==1):
		 #time.sleep(10)
                 proc.stdin.write('ivtree123\n')
                 print "entered password"
		 proc.stdin.write('Y\n')
                 print "Accepted by entering Y"

            print "before wait"
            proc.wait()
            print "after wait"
            output=proc.stdout.read()
	    print "Current command "+gluster_deletion+" output is\n" + output
            logging.debug("process output "+str(i)+" is "+output)
	    #logging.info('successfully deleted gluster')
	    flag=True

        except subprocess.CalledProcessError as e:
            print "Called Process Error while executing command"
	    fag=False
    if(flag==True):
	logging.info('Command successfully run for deleted gluster')
    else:
        logging.info('Command fails')
    #Deleting gluster info
    p1=subprocess.Popen(['sudo rm -rf /etc/apt/sources.list.d/gluster.list'], shell=True, stdout=subprocess.PIPE)
    p1.wait()
    # Removing locks
    p2=subprocess.Popen(['sudo rm /var/lib/dpkg/lock'],shell=True, stdout=subprocess.PIPE)
    p2.wait()

def fio_start():
    try:
        logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)-10s) %(message)s', )
        proc=subprocess.Popen(['fio --name=randwrite --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=0 --size=512M --numjobs=8 --runtime=240 --group_reporting'], shell=True, stdout=subprocess.PIPE)
       	print "before wait"
        proc.wait()
        print "after wait"
        logging.debug("fio jobs started")
        output = proc.stdout.read()
        logging.debug("process output is " + output)
	#logging.info('successfully completed fio')
	print "Current command output is" + output
        flag=True

    except subprocess.CalledProcessError as e:
        print "Called Process Error while executing command"
	flag=False
    if(flag==True):
	logging.info('Command successfully run for fio start')
    else:
        logging.info('Command fails')

def fio_install():
    try:
        logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)-10s) %(message)s', )
        proc=subprocess.Popen(['apt-get --yes install fio'], shell=True, stdout=subprocess.PIPE)
	print "before wait"
        proc.wait()
        print "after wait"
        logging.debug("fio successfully installed")
        output = proc.stdout.read()
        logging.debug("process output is " + output)
	#logging.info('successfully installed fio')
	print "Current command output is" + output
        flag=True

    except subprocess.CalledProcessError as e:
        print "Called Process Error while executing command"
    if(flag==True):
        logging.info('Command successfully run for fio install')
    else:
        logging.info('Command fails')

def add_storage():
    std=["cd",
         "sudo fdisk /dev/sdb1",
         "n",
         "p",
         "1"
         "\n",
         "\n",
         "p",
         "w",
         "sudo mkfs.ext4 /dev/sdb1",
         "sudo mkdir -p /data/gluster2",
         "sudo mount /dev/sdb1 /data/gluster2",
         "echo "+"/dev/sdb1 /data/gluster2 ext4 defaults 0 0"+" | sudo tee --append /etc/fstab"]
    for i in range(len(std)):
        try:
            logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
            proc=subprocess.Popen([std[i]], shell=True, stdout=subprocess.PIPE)
            if(i==1):
                 #time.sleep(10)
                 proc.stdin.write('ivtree123\n')
                 print "entered password"
                 proc.stdin.write('Y\n')
                 print "Accepted by entering Y"

	    print "before wait"
            proc.wait()
            print "after wait"
            output=proc.stdout.read()
            logging.debug("process output "+str(i)+" is "+output)
	    #logging.info('successfully created storage')


        except subprocess.CalledProcessError as e:
            print "Called Process Error while executing command"

if __name__ == '__main__':

    print "programing start"
    # pinging()
    #creategluster()
    #gluster_status()
    # delete_gluster()
    # fio_install()
    # fio_start()
    #add_storage()
    #add_storage()

