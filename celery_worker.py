from datetime import datetime
from time import sleep


def celery_worker(data_processor_number: int, data: int):
    sleep(0.5)

    result = f'data processor {data_processor_number} - data {data} - {datetime.now().time()}'
    print(result)

    return result


if __name__ == '__main__':
    print(celery_worker(1, 1))
