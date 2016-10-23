import pytest
from hamcrest import assert_that, is_


# noinspection PyPep8Naming
@pytest.mark.usefixtures("TestinfraBackend")
@pytest.mark.dockerfile(path='commands')
class TestAlpainEnvironmentTest(object):
    def test_curl_exists(self, Command):
        assert_that(Command('curl --help').rc, is_(0))

    def test_docker_exists(self, Command):
        assert_that(Command('docker').rc, is_(0))