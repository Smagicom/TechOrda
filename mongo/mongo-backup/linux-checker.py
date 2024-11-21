TAR_SOLUTION="""
reservations/
reservations/user_reservations.bson
reservations/rooms.metadata.json
reservations/user_reservations.metadata.json
reservations/users.bson
reservations/users.metadata.json
reservations/rooms.bson
"""

def test_tar(s):
    stdout = s.run("ls /home/box/reservations-dump.tar.gz")
    assert stdout.succeeded, "/home/box/reservations-dump.tar.gz is not present"

def test_tar_files(s):
    lines = TAR_SOLUTION.strip().split("\n")
    cmd = "tar -tf /home/box/reservations-dump.tar.gz"
    stdout = s.run(cmd)
    for line in lines:
        assert line in stdout, line+" is not present in reservations-dump.tar.gz"
