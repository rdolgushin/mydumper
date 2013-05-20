Simple MySQL dumper
===================

Mydumper allows you:

* To make dumps of MySQL databases
* Automaticaly remove outdated or unnecessary of stored dumps

Installation
------------

> Is recommended to install syncle with [pip](http://www.pip-installer.org) and [virtualenv](http://www.virtualenv.org/), but you can also use any other [method](http://wiki.python.org/moin/CheeseShopTutorial) of Python package installing.

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

When using mydumper (installed with pip and virtualenv) with cron it can be necessary
to source virtualenv activate script before. For example:

```shell
# Crontab
0 */1 * * * * source /home/john/.virtualenvs/default/bin/activate && mydumper -u john -p secret -m 10 -M 3 test_db
```
