CREATE ROLE pghero WITH LOGIN PASSWORD 'pghero_password' SUPERUSER;
CREATE DATABASE deadline WITH owner pghero;

CREATE extension pg_stat_statements;
