def test_reservations(s):
    cmd = """
mongo -u "admin" -p "singularity" --authenticationDatabase admin << EOF 2>/dev/null
use reservations
db.getCollectionNames()
EOF
    """
    stdout = s.run(cmd)
    exp = '[ "rooms", "user_reservations", "users" ]'
    assert exp in stdout, "reservations database is not restored"
