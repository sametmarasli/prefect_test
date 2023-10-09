from prefect.filesystems import LocalFileSystem
from prefect.infrastructure import Process
from prefect.filesystems import GitHub

my_storage_block = LocalFileSystem(basepath = '/home/samet/prefect-tutorial')
my_storage_block.save(name='storage-block', overwrite=True)

# my_process_infra = Process()
# my_process_infra.save(name='process-infra', overwrite=True)



block = GitHub(
    repository="https://github.com/sametmarasli/prefect_test.git",
    include_git_objects=False,
)

block.save("git-storage-block", overwrite=True)