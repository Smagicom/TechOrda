def test_apt_postgresql(s):
    cmd = "sudo -iu postgres psql --version 2>/dev/null | cut -d ' ' -f 3"
    stdout = s.run(cmd)
    version = float(stdout)
    
    assert version >= 14, "Wrong postgresql version"
