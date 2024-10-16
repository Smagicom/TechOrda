def test_apt_nginx(s):
    cmd = "sudo nginx -v"
    stdout = s.run(cmd)
    versions = stdout.strip().split("/")[-1].split(".")
    a, b = versions[0], versions[1]
    
    assert float(a) >= 1 and float(b) >= 20, "Wrong nginx version"

