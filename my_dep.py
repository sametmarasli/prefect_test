from my_flow import dog
from prefect.deployments import Deployment
from prefect.filesystems import LocalFileSystem

storage_block = LocalFileSystem.load('storage-block')


deployment = Deployment.build_from_flow(
    flow=dog,
    name="dep-from-python",
    parameters={"num_barks":3},
    storage=storage_block
    )


deployment.apply()
