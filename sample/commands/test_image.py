import pytest
from hamcrest import assert_that, is_


# noinspection PyPep8Naming
@pytest.mark.usefixtures("host")
@pytest.mark.dockerfile(path='commands')
class TestAlpainEnvironmentTest(object):
    def test_curl_exists(self, host):
        assert_that(host.run('curl --help').rc, is_(0))

    def test_docker_exists(self, host):
        assert_that(host.run('docker').rc, is_(0))