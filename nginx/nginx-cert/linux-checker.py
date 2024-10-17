def test_cert(s):
    exp = "C=KZ; ST=Nur-Sultan; L=Nur-Sultan; O=Jusan Singularity; OU=Track Devops; CN=track-devops"
    cmd = 'curl -H "Host: jusan.kz" -svI -k https://localhost/secret_word  2>&1 | grep issuer'
    stdout = s.run(cmd)
    assert exp in stdout, "certificate not installed"

def test_output(s):
    exp = "jusan-nginx-cert"
    cmd = 'curl -H "Host: jusan.kz" -k https://localhost/secret_word'
    stdout = s.run(cmd)
    assert stdout.strip() == exp, "wrong output:"+stdout

