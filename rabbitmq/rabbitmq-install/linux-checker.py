def test_mongodb(s):
    cmd = "rabbitmqctl --version"
    stdout = s.run(cmd)
    major, minor = stdout.split('.',1)
    major = float(major)
    minor = float(minor)
    assert major >= 3 and minor >= 9, "rabbitmq incorrectly installed"

def test_management(s):
    cmd = 'curl -sI localhost:15672 | head -n1'
    stdout = s.run(cmd)
    exp = "HTTP/1.1 200 OK"
    
    assert exp in stdout, "management plugin not enabled"

