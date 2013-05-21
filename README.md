Simple MySQL dumper
===================

Mydumper allows you:

* To make dumps of MySQL databases
* Automaticaly remove outdated or unnecessary of stored dumps

Installation
------------

> Is recommended to install mydumper with [pip](http://www.pip-installer.org) and [virtualenv](http://www.virtualenv.org/), but you can also use any other [method](http://wiki.python.org/moin/CheeseShopTutorial) of Python package installing.

### From PyPI

    $ pip install mydumper

### From Git sources

    $ git clone git://github.com/rdolgushin/mydumper.git
    $ pip install -e mydumper/

Usage
-----

    $ mydumper
    usage: mydumper -u USER [-p PASSWORD] [-h HOST] -d DUMP_DIR
                    [-m MAX_DUMPS_QTY] [-M MAX_DAYS_DELTA]
                    database
    $ mydumper -u john -p secret -m 10 -M 3 test_db

If you will use mydumper installed with pip and virtualenv in crontab file
it will looks like following example:

```shell
# Crontab
0 */1 * * * * /home/john/.virtualenvs/default/bin/mydumper -u john -p secret -m 10 -M 3 test_db
```

See also
--------

* [Pgdumper](https://github.com/rdolgushin/pgdumper)
