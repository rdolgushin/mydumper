#!/usr/bin/env python

import os, time
from datetime import datetime, timedelta
import argparse

class Dumper():

    def __init__(self, description, dump_cmd_pattern, with_password=True):
        self.description = description
        self.dump_cmd_pattern = dump_cmd_pattern
        self.with_password = with_password

    def make_dump(self, user, password, db, host, dump_dir):
        date_string = str(datetime.now()).replace(" ", "_")
        dump_file = "%s__%s.sql" % (db, date_string)
        dump_file = os.path.join(dump_dir, dump_file)

        dump_cmd = self.dump_cmd_pattern % {
            "user": user, "password": password,
            "host": host, "db": db, "dump_file": dump_file
        }

        os.system(dump_cmd)

    def clear_dumps(self, db, dump_dir, max_dumps_qty, max_days_delta):
        dumps = []
        for dump_file in os.listdir(dump_dir):
            if dump_file.startswith("%s__" % db):
                date_begin = len(db) + 2
                date_string = dump_file[date_begin:]
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

    def run(self):
        parser = argparse.ArgumentParser(
            description=self.description,
            add_help=False
        )

        parser.add_argument("database")
        parser.add_argument("-u", "--user", required=True)
        if self.with_password:
            parser.add_argument("-p", "--password", default='')
        parser.add_argument("-h", "--host", default='localhost')
        parser.add_argument("-d", "--dump-dir", required=True)
        parser.add_argument("-m", "--max-dumps-qty", type=int, default=14)
        parser.add_argument("-M", "--max-days-delta", type=int, default=7)

        args = parser.parse_args()

        db = args.database
        user = args.user
        host = args.host

        if self.with_password:
            password = args.password
        else:
            password = ''

        dump_dir = os.path.expanduser(args.dump_dir)
        max_dumps_qty = args.max_dumps_qty
        max_days_delta = args.max_days_delta

        self.make_dump(user,password,db,host,dump_dir)
        self.clear_dumps(db,dump_dir,max_dumps_qty,max_days_delta)

def main():
    dumper = Dumper(
        "Simple MySQL dumper.",
        "mysqldump -u %(user)s -p%(password)s -h %(host)s %(db)s > %(dump_file)s"
    )
    dumper.run()
