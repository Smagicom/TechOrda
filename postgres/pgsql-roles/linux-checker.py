def test_groups(s):
    groups = ['administrator', 'student']
    cmd = "sudo -iu postgres psql -U {} deadline"
    for group in groups:
        stdout = s.run(cmd.format(group))        
        assert stdout.return_code == 2, group+" is not a group"

def test_user_groups(s):
    user_groups = [
        ('arman', ['administrator']),
        ('dias', ['administrator']),
        ('artem', ['student']),
        ('lyazzat', ['student']),
        ('askhat', ['administrator', 'student']),
    ]
    cmd = "sudo -iu postgres psql -U postgres deadline -c '\du' | grep {}"
    for (user, groups) in user_groups:
        stdout = s.run(cmd.format(user))
        for group in groups:        
            assert group in stdout, user+" in not member of group "+group

def test_user_password(s):
    user_passwds = [
        ('arman', 'M96pgz3h'),
        ('dias', 'sxr9hN5h'),
        ('artem', 'UD4z3Evu'),
        ('lyazzat', 'PG9ku65k'),
    ]
    cmd = "sudo -iu postgres psql \"postgresql://{}:{}@127.0.0.1/deadline\" -c 'SELECT 1'"
    for (user, passwd) in user_passwds:
        stdout = s.run(cmd.format(user, passwd))        
        assert stdout.succeeded, user+" has incorrect password"

def test_group_grants(s):
    group_permissions = [
        ('administrator', ['TRIGGER', 'INSERT', 'SELECT', 'UPDATE', 'DELETE', 'TRUNCATE', 'REFERENCES']),
        ('student', ['SELECT'])
    ]
    query = """sudo -iu postgres psql -U postgres -c \"
    SELECT grantee, string_agg(privilege_type, ', ') 
    FROM information_schema.role_table_grants 
    WHERE table_name='deadline' and grantee='{}' group by grantee
    \"
    """.replace("\n", '')
    for (group, permissions) in group_permissions:
        stdout = s.run(query.format(group))
        for permission in permissions:
            assert permission in stdout, group+" has no permission - "+permission

def test_pg_hba(s):
    rules = [
        ('host', 'deadline', '+administrator', '127.0.0.1', '255.255.255.0', 'md5'),
        ('host', 'all', ' askhat', 'all', '0', 'reject'),
        ('host', 'deadline', '+student', '127.0.0.1', '255.255.255.0', 'scram-sha-256'),
        ('host', 'all', ' postgres', 'all', '0', 'md5'),
    ]
    cmd = "sudo -iu postgres psql -U postgres -c \"select type,database,user_name,address,netmask,auth_method from pg_hba_file_rules where type='{}' AND '{}'=ANY(database) AND  '{}'=ANY(user_name) AND address='{}' AND netmask='{}' AND auth_method='{}'\""
    i = 1
    for rule in rules:
        stdout = s.run(cmd.format(rule[0], rule[1], rule[2], rule[3], rule[4], rule[5]))
        assert int(stdout) == 1, "no pg_hba rule#"+i
        i += 1
