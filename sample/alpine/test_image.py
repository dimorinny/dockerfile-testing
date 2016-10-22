import pytest


# noinspection PyPep8Naming
@pytest.mark.usefixtures("TestinfraBackend")
@pytest.mark.dockerfile(package='alpine')
class TestAlpainEnvironmentTest(object):
    def test_curl_exists(self, Command):
        Command.run_expect(expected=[0], command="curl --help")

    def test_docker_exists(self, Command):
        Command.run_expect(expected=[0], command="docker")
