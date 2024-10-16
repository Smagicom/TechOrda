request_sizes = [
    ("http://localhost:8080/images/sleep.png","5347316"),
    ("http://localhost:8080/images/flower.png","6173737"),
    ("http://localhost:8080/images/glasses.png","4996355"),
    ("http://localhost:8080/images/gray-animal.jpeg","458964"),
    ("http://localhost:8080/images/mafia.png","3772725"),
    ("http://localhost:8080/gifs/sad.gif", "3605836"),
    ("http://localhost:8080/gifs/jam.gif", "471720"),
    ("http://localhost:8080/gifs/dancing.gif", "253794"),
    ("http://localhost:8080/", "729"),
    ("http://localhost:8080/secret_word", "21"),
]

def test_request_sizes(s):
    req = "curl -sI -H 'Host: example.com' {} | grep Content-Length | cut -d ':' -f2"

    for _, (url, size) in enumerate(request_sizes):
        stdout = s.run(req.format(url))
        assert stdout.strip() == size.strip(), "error on request: {}".format(url)
