import psutil
import logging
import time

cpu_limit = 80
mem_limit = 80
disk_limit = 90

logging.basicConfig(stream=sys.stdout, filename='sys_health.log', level=logging.WARNING)

def check_cpu():
    cpu_usage = psutil.cpu_percent()
    if cpu_usage > cpu_limit:
        logging.warning(f'CPU usage exceeded {cpu_limit}%: {cpu_usage}%')

def check_memory():
    mem_usage = psutil.virtual_memory().percent
    if mem_usage > mem_limit:
        logging.warning(f'Memory usage exceeded {mem_limit}%: {mem_usage}%')

def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > disk_limit:
        logging.warning(f'Disk usage exceeded {disk_limit}%: {disk_usage}%')

def process():
    running_processes = len(psutil.pids())
    logging.info(f'Running processes: {running_processes}')

def main():
    while True:
        check_cpu()
        check_memory()
        check_disk()
        process()
        time.sleep(60)

if __name__ == '__main__':
    main()