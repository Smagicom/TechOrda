SOLUTION = """
max_connections = 300
shared_buffers = 128MB
effective_cache_size = 384MB
maintenance_work_mem = 32MB
checkpoint_completion_target = 0.9
wal_buffers = 3932kB
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = 200
work_mem = 436kB
min_wal_size = 2GB
max_wal_size = 8GB
max_worker_processes = 2
max_parallel_workers_per_gather = 1
max_parallel_workers = 2
max_parallel_maintenance_workers = 1
"""

def check(reply):
    confs = [line for line in SOLUTION.strip().split("\n") if line]
    for conf in confs:
        if conf not in reply:
            return False
    return True
