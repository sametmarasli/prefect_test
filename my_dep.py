from my_flow import dog
from prefect.deployments import Deployment
from prefect.filesystems import GitHub, LocalFileSystem
from prefect.infrastructure import Process

storage_block =GitHub.load('git-storage-block')
# storage_block =LocalFileSystem.load('storage-block')
# infra_block =Process.load('process-infra')


deployment = Deployment.build_from_flow(
    flow=dog,
    name="dep-from-python",
    parameters={"num_barks":3},
    storage=storage_block,
    )


deployment.apply()
