request_sizes = [
    ("design:SteveJobs1955", "http://localhost:8080/images/sleep.png","5347316"),
    ("design:SteveJobs1955", "http://localhost:8080/images/flower.png","6173737"),
    ("design:SteveJobs1955", "http://localhost:8080/images/glasses.png","4996355"),
    ("design:SteveJobs1955", "http://localhost:8080/images/gray-animal.jpeg","458964"),
    ("design:SteveJobs1955", "http://localhost:8080/images/mafia.png","3772725"),
    ("marketing:marketingP@ssword", "http://localhost:8080/gifs/sad.gif", "3605836"),
    ("marketing:marketingP@ssword", "http://localhost:8080/gifs/jam.gif", "471720"),
    ("marketing:marketingP@ssword", "http://localhost:8080/gifs/dancing.gif", "253794"),
    ("marketing:marketingP@ssword", "http://localhost:8080/", "729"),
]

denied_requests = [
    ("marketing:marketingP@ssword", "http://localhost:8080/images/sleep.png"),
    ("design:SteveJobs1955", "http://localhost:8080/gifs/dancing.gif"),
    ("security:CuteCats<33", "http://localhost:8080/gifs/dancing.gif"),
    ("security:CuteCats<33", "http://localhost:8080/images/sleep.png"),
]

def test_request_sizes(s):
    req = "curl -sI -u '{}' -H 'Host: example.com' {} | grep Content-Length | cut -d ':' -f2"

    for _, (cred, url, size) in enumerate(request_sizes):
        stdout = s.run(req.format(cred, url))
        assert stdout.strip() == size.strip(), \
            "error on request: {}\nno access for {}".format(url, cred)

def test_denied_requests(s):
    req = "curl -sI -u '{}' -H 'Host: example.com' {} | head -n1"

    for _, (cred, url) in enumerate(denied_requests):
        stdout = s.run(req.format(cred, url))
        assert "401 Unauthorized" in stdout.strip(), "oops, user {} has access to {}".format(cred, url)

def test_root(s):
    req = "curl -sI http://localhost:8080/ | head -n1"
    stdout = s.run(req)
    expected = "HTTP/1.1 200 OK"
    assert stdout.strip() == expected, "http://localhost:8080/ is blocked"
