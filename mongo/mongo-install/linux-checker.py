def test_mongodb(s):
    cmd = "mongod --version | head -n1"
    stdout = s.run(cmd)
    exp = "db version"
    
    assert exp in stdout, "mongodb incorrectly installed"

def test_admin(s):
    cmd = 'mongo -u "admin1" -p "singularit1y" --authenticationDatabase "admin" --eval "print()"'
    stdout = s.run(cmd)
    
    assert stdout.succeeded, "no admin user is created!"

