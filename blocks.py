from prefect.filesystems import LocalFileSystem
from prefect.infrastructure import Process

my_storage_block = LocalFileSystem(basepath = '~/cat')
my_storage_block.save(name='storage-block', overwrite=True)

my_process_infra = Process(working_dir = '~/prefect-tutorial')
my_process_infra.save(name='process-infra', overwrite=True)