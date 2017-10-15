from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(host):
    present = [
        "/etc/nginx",
        "/etc/nginx/snippets",
        "/etc/nginx/sites-enabled",
        "/etc/nginx/sites-available",
        "/var/www/custom_error_pages",
        "/var/log/nginx"
    ]
    if present:
        for directory in present:
            d = host.file(directory)
            if directory == "/var/log/nginx":
                assert d.mode == 0o755
            assert d.is_directory
            assert d.exists


def test_files(host):
    present = [
        "/etc/nginx/nginx.conf",
        "/etc/nginx/snippets/ssl.conf",
        "/etc/nginx/snippets/errors.conf",
        "/etc/nginx/snippets/headers.conf",
        "/etc/nginx/snippets/proxy.conf",
        "/etc/nginx/snippets/letsencrypt.conf",
        "/var/www/custom_error_pages/nginx_400.html",
        "/var/www/custom_error_pages/nginx_403.html",
        "/var/www/custom_error_pages/nginx_404.html",
        "/var/www/custom_error_pages/nginx_405.html",
        "/var/www/custom_error_pages/nginx_408.html",
        "/var/www/custom_error_pages/nginx_411.html",
        "/var/www/custom_error_pages/nginx_429.html",
        "/var/www/custom_error_pages/nginx_500.html",
        "/var/www/custom_error_pages/nginx_502.html",
        "/var/www/custom_error_pages/nginx_503.html",
        "/var/www/custom_error_pages/nginx_504.html",
        "/etc/nginx/dhparam.pem"
    ]
    absent = [
        "/etc/nginx/sites-enabled/default"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file
    if absent:
        for file in absent:
            d = host.file(file)
            assert not d.exists


def test_service(host):
    present = [
        "nginx",
        "nginx_exporter"
    ]
    if present and host.system_info.distribution == 'ubuntu':
        for service in present:
            s = host.service(service)
            assert s.is_enabled
            assert s.is_running


def test_packages(host):
    present = [
        "nginx"
    ]
    if present:
        for package in present:
            p = host.package(package)
            assert p.is_installed


def test_socket(host):
    assert host.socket('tcp://127.0.0.1:9113').is_listening
    assert host.socket('tcp://127.0.0.1:8060').is_listening
    assert host.socket('tcp://127.0.0.1:80').is_listening
