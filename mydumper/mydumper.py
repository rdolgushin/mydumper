#!/usr/bin/env python

import os, time
from datetime import datetime, timedelta
import argparse

parser = argparse.ArgumentParser(
    description="Simple MySQL dumper.",
    add_help=False
)

parser.add_argument("database")
parser.add_argument("-u", "--user", required=True)
parser.add_argument("-p", "--password", default='')
parser.add_argument("-h", "--host", default='localhost')
parser.add_argument("-d", "--dump-dir", required=True)
parser.add_argument("-m", "--max-dumps-qty", type=int, default=14)
parser.add_argument("-M", "--max-days-delta", type=int, default=7)

args = parser.parse_args()

db = args.database
user = args.user
password = args.password
host = args.host

dump_dir = os.path.expanduser(args.dump_dir)
max_dumps_qty = args.max_dumps_qty
max_days_delta = args.max_days_delta

def make_dump():
    date_string = str(datetime.now()).replace(" ", "_")
    dump_file = "%s-%s.sql" % (db, date_string)
    dump_file = os.path.join(dump_dir, dump_file)

    dump_cmd = "mysqldump -u %s -p%s -h %s %s > %s" % (user, password, host, db, dump_file)

    os.system(dump_cmd)

def clear_dumps():
    dumps = []
    for dump_file in os.listdir(dump_dir):
        date_string = "_".join(dump_file.split("_")[1:])
        dumps.append(
            (dump_file, datetime.strptime(date_string, "%Y-%m-%d_%H:%M:%S.%f.sql"))
        )
    dumps = sorted(dumps, key=lambda dump: dump[1])
    dumps.reverse()

    to_delete_1 = [] # Deleting by max qty
    to_delete_2 = [] # Deleting by max days delta

    if max_dumps_qty:
        for i, dump in enumerate(dumps):
            if i > max_dumps_qty - 1:
                to_delete_1.append(dump)
        for dump in to_delete_1:
            dumps.remove(dump)

    if max_days_delta:

        cut_date = datetime.now() - timedelta(days=max_days_delta)

        for dump in dumps:
            if dump[1] < cut_date:
                to_delete_2.append(dump)
        for dump in to_delete_2:
            dumps.remove(dump)

    to_delete = to_delete_1
    to_delete.extend(to_delete_2)

    for dump in to_delete:
        dump_path = os.path.join(dump_dir, dump[0])
        os.remove(dump_path)

def main():
    make_dump()
    clear_dumps()
