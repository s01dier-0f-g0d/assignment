import paramiko
import os
import logging

host = 'kali'
usrname = 'abc'
pwd = '123'
remote_path = '/root/home/apache/remote/backup'

local_dir = '/home/abc/backup'

def ssh_backup():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=usrname, password=pwd)

    sftp = ssh.open_sftp()
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_file = os.path.join(root, file)
            remote_file = os.path.join(remote_path, os.path.relpath(local_file, local_dir))
            sftp.put(local_file, remote_file)

    sftp.close()
    ssh.close()

    logging.info('Backup to remote server successful')

logging.basicConfig(filename='backup.log', level=logging.INFO)

if __name__ == '__main__':
    try:
        ssh_backup()
    except Exception as e:
        logging.error(f'Backup failed: {e}')