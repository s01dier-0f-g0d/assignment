import requests
import time
import logging

url = 'https://google.com'

code = [200, 201, 202]

logging.basicConfig(filename='app_status.log', level=logging.INFO)

def check_status():
    try:
        response = requests.get(url, timeout=10)
        if response.status_code in code:
            logging.info(f'Application is UP: {response.status_code}')
            return 'UP'
        else:
            logging.warning(f'Application is DOWN: {response.status_code}')
            return 'DOWN'
    except requests.exceptions.RequestException as e:
        logging.error(f'Application is DOWN: {e}')
        return 'DOWN'

def main():
    while True:
        status = check_status()
        print(f'Application status: {status}')
        time.sleep(60)

if __name__ == '__main__':
    main()
