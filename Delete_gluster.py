import subprocess

def deletegluster():
    proc=subprocess.Popen(['sudo apt-get uninstall -y glusterfs-server'],stdout=subprocess.PIPE)