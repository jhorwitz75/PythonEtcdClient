import os

HOST_FAIL_WAIT_S = 5
"Number of seconds that must elapse before we're allowed to retry a host."

ATOMIC_MAX_ATTEMPTS = int(os.environ.get('ETCD_ATOMIC_MAX_ATTEMPTS', '5'))
