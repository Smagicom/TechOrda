def test_dump(s):
    cmd = "md5sum /home/box/backup_deadline.sql | cut -d ' ' -f1"
    expected_md5="2dd88c9bdff930903d6be8a6f210070e"
    stdout = s.run(cmd)
    assert stdout.strip() == expected_md5, "invalid backup_deadline.sql"

def test_restore(s):
    cmd = "sudo -iu postgres psql -U postgres -c '\l+' | grep deadline_test"
    stdout = s.run(cmd)
    assert "10 MB" in stdout, "deadline_test is not restored properly from deadline"
