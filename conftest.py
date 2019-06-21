import pytest
import testinfra

check_output = testinfra.get_host(
    'local://'
).check_output


# noinspection SpellCheckingInspection
def pytest_addoption(parser):
    parser.addoption(
        '--squash',
        action='store_true',
        help='Use squash option for building docker image'
    )


@pytest.fixture()
def host(request):
    arguments = '--squash' if request.config.getoption('--squash') else ''

    build_command = 'docker build {arguments} --quiet {path}'.format(
        arguments=arguments,
        path=request.param
    )
    image_id = check_output(build_command)

    run_command = 'docker run --detach --entrypoint tail {image_id} -f /dev/null'.format(
        image_id=image_id
    )
    container_id = check_output(run_command)

    def teardown():
        check_output('docker rm -f %s', container_id)

    request.addfinalizer(teardown)

    return testinfra.get_host('docker://' + container_id)


# noinspection SpellCheckingInspection
def pytest_generate_tests(metafunc):
    if 'host' in metafunc.fixturenames:

        marker = metafunc.definition.get_closest_marker('dockerfile')

        path = marker.kwargs.get('path')
        if path is None:
            path = '.'

        metafunc.parametrize(
            'host',
            [path],
            indirect=True,
            scope='module'
        )
