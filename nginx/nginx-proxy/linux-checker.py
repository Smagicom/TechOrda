def test_api(s):
    cmd = "curl http://localhost/api/"

    stdout = s.run(cmd)
    if "web-server" not in stdout:
        assert False, "wrong response from nginx:\n{}".format(stdout)

    web1, cnt1 = stdout.strip().split(":")

    stdout = s.run(cmd)
    web2, cnt2 = stdout.strip().split(":")

    stdout = s.run(cmd)
    web3, cnt3 = stdout.strip().split(":")

    assert web1 == web2 and web2 == web3 and web3 == "web-server", \
        "wrong response:\n{}\n{}\n{}\n".format(web1, web2, web3)
    
    assert int(cnt1) < int(cnt2) and int(cnt2) < int(cnt3), \
        "wrong response:\n{}\n{}\{}\n".format(cnt1, cnt2, cnt3)
