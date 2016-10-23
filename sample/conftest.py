import pytest
import testinfra

check_output = testinfra.get_backend(
    "local://"
).get_module("Command").check_output


# noinspection PyPep8Naming
@pytest.fixture()
def TestinfraBackend(request):
    # Build image
    image_id = check_output("docker build -q %s", request.param)

    # Run container
    container_id = check_output(
        "docker run -d %s tail -f /dev/null", image_id
    )

    def teardown():
        check_output("docker rm -f %s", container_id)

    # Destroy the container at the end of the fixture life
    request.addfinalizer(teardown)

    # Return a dynamic created backend
    return testinfra.get_backend("docker://" + container_id)


def pytest_generate_tests(metafunc):
    if "TestinfraBackend" in metafunc.fixturenames:

        marker = getattr(metafunc.function, "dockerfile", None)

        path = marker.kwargs.get('path')
        if path is None:
            path = '.'

        metafunc.parametrize(
            "TestinfraBackend", [path], indirect=True, scope='module')
