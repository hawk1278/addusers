import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("ro1423")
    assert passwd.user == "ro1423"
    assert passwd.group == "ro1423"
    assert passwd.mode == 0o644
