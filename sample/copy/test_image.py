import pytest


# noinspection PyPep8Naming
@pytest.mark.usefixtures("TestinfraBackend")
@pytest.mark.dockerfile(path='copy/docker')
class TestAlpainEnvironmentTest(object):
    COPIED_FILE_PATH = '/dir/file.txt'
    COPIED_FILE_CONTENT = 'dimorinny'

    def test_copied_file_exists(self, File):
        assert File(self.COPIED_FILE_PATH).exists

    def test_copied_file_content(self, File):
        assert File(self.COPIED_FILE_PATH).content_string == self.COPIED_FILE_CONTENT
