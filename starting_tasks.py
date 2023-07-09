from multiprocessing import Process, Manager
from queue import Queue

from tasks import task


def data_processing(
        data_processor_number: int,
        data_list: list,
        answers: Queue
):
    print(
        f'\n'
        f'data processor {data_processor_number} start with {data_list}',
        end=''
    )

    result = []

    for i in range(len(data_list)):
        result.append(
            task.delay(data_processor_number, data_list[i])
        )

    answers.put(result)


def starting_tasks(
        data_amount: int,
        processes_number: int,
):
    process = []
    tasks_result = []

    mproc_manager = Manager()
    answers = mproc_manager.Queue()

    data = list(range(data_amount))
    print(
        f'\n'
        f'initial data - {data}'
    )

    part_size = -1 * data_amount // processes_number * -1

    for data_processor_number in range(processes_number):
        part_of_data = data[
                       part_size * data_processor_number:
                       part_size * (data_processor_number + 1)
                       ]

        process.append(
            Process(
                target=data_processing,
                args=(
                    data_processor_number,
                    part_of_data,
                    answers,
                )
            )
        )

    [p.start() for p in process]
    [p.join() for p in process]

    while not answers.empty():
        tasks_result += answers.get()

    return tasks_result


if __name__ == '__main__':
    starting_tasks(
        data_amount=11,
        processes_number=3,
    )
