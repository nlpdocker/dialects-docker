dialects-docker
===============

This is my attempt at getting Alex Magidow's [Database of Arabic Dialects](https://github.com/amagidow/dialects)
running in a Docker container.

Installation
============

``docker build -t dialects https://github.com/nlpdocker/dialects-docker.git``


Usage
=====

Unfortunately, this doesn't work yet. See [this Github issue](https://github.com/amagidow/dialects/issues/1) for details.

```bash
# start the container
docker run -ti dialects

$ ~/repos/nlpdocker/dialects-docker $ docker run -ti dialects
 * Starting PostgreSQL 9.3 database server                                                                                                                       [ OK ] 

[...]

Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/django/utils/autoreload.py", line 223, in wrapper
    fn(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/django/core/management/commands/runserver.py", line 112, in inner_run
    self.check_migrations()
  File "/usr/local/lib/python3.4/dist-packages/django/core/management/commands/runserver.py", line 164, in check_migrations
    executor = MigrationExecutor(connections[DEFAULT_DB_ALIAS])
  File "/usr/local/lib/python3.4/dist-packages/django/db/migrations/executor.py", line 19, in __init__
    self.loader = MigrationLoader(self.connection)
  File "/usr/local/lib/python3.4/dist-packages/django/db/migrations/loader.py", line 47, in __init__
    self.build_graph()
  File "/usr/local/lib/python3.4/dist-packages/django/db/migrations/loader.py", line 180, in build_graph
    self.applied_migrations = recorder.applied_migrations()
  File "/usr/local/lib/python3.4/dist-packages/django/db/migrations/recorder.py", line 59, in applied_migrations
    self.ensure_schema()
  File "/usr/local/lib/python3.4/dist-packages/django/db/migrations/recorder.py", line 49, in ensure_schema
    if self.Migration._meta.db_table in self.connection.introspection.table_names(self.connection.cursor()):
  File "/usr/local/lib/python3.4/dist-packages/django/db/backends/base/base.py", line 162, in cursor
    cursor = self.make_debug_cursor(self._cursor())
  File "/usr/local/lib/python3.4/dist-packages/django/db/backends/base/base.py", line 135, in _cursor
    self.ensure_connection()
  File "/usr/local/lib/python3.4/dist-packages/django/db/backends/base/base.py", line 130, in ensure_connection
    self.connect()
  File "/usr/local/lib/python3.4/dist-packages/django/db/utils.py", line 97, in __exit__
    six.reraise(dj_exc_type, dj_exc_value, traceback)
  File "/usr/local/lib/python3.4/dist-packages/django/utils/six.py", line 658, in reraise
    raise value.with_traceback(tb)
  File "/usr/local/lib/python3.4/dist-packages/django/db/backends/base/base.py", line 130, in ensure_connection
    self.connect()
  File "/usr/local/lib/python3.4/dist-packages/django/db/backends/base/base.py", line 119, in connect
    self.connection = self.get_new_connection(conn_params)
  File "/usr/local/lib/python3.4/dist-packages/django/db/backends/postgresql_psycopg2/base.py", line 176, in get_new_connection
    connection = Database.connect(**conn_params)
  File "/usr/local/lib/python3.4/dist-packages/psycopg2/__init__.py", line 164, in connect
    conn = _connect(dsn, connection_factory=connection_factory, async=async)
django.db.utils.OperationalError: FATAL:  database "arabicDialectProject" does not exist
```

