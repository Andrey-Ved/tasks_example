from redis import Redis

from starting_tasks import starting_tasks


def print_redis_keys() -> None:
    try:
        with Redis(
                host='localhost',
                port=6379,
                charset="utf-8",
                decode_responses=True
        ) as r:
            print(
                f'\n'
                f'Redis keys:'
            )
            if len(r.keys()):
                [print(f'{n} - {k}') for n, k in enumerate(r.keys())]
            else:
                print('base is empty')

    except Exception as e:
        print(e)


def main():
    print_redis_keys()

    tasks_result = starting_tasks(
        data_amount=10,
        processes_number=3,
    )

    print(
        f'\n\n'
        f'tasks is started'
        f'\n'
    )

    [
        print(f'task {n} - {i.get()}')
        for n, i in enumerate(tasks_result)
    ]

    print_redis_keys()

    print(
        f'\n'
        f'results cleaning in Redis'
    )

    [i.forget() for i in tasks_result]

    print_redis_keys()


if __name__ == '__main__':
    main()
