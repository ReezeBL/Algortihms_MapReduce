#!/usr/bin/env python

import mincemeat
import sys
from multiprocessing import Pool, Process

client_num = 4
sleep_time = 2

def run_client(options = {}):
    while True:
        try:
            client = mincemeat.Client()
            client.password = bytes('', "utf-8")
            client.conn('localhost', mincemeat.DEFAULT_PORT)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    if len(sys.argv) > 1:
        client_num = int(sys.argv[1])
    procs = []
    for i in range(client_num):
        procs.append(Process(target=run_client))
    for i in range(client_num):
        procs[i].start()
    for i in range(client_num):
        procs[i].join()