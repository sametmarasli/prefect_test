from prefect import flow, task, get_run_logger

@task
def speak():
    # logger = get_run_logger()
    # logger.info('Woof!')
    get_run_logger().info('Woof!')

@flow
def dog(num_barks:int):
    for i in range(num_barks):
        speak()

if __name__ == "__main__":
    dog(3)