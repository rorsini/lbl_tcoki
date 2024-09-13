#!/usr/bin/env python

from tcoki import profileTcoki
import pprint
import click
import json

def read_json_file(jsonfile):
    content = None
    with open(jsonfile) as f:
        content = json.load(f)
    return content

@click.command()
@click.option('--jsonfile')
def init(jsonfile):
    """
    jsonfile is an input filepath
    """
    content = read_json_file(jsonfile)
    if content:
        res = profileTcoki(content)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(res)

if __name__ == "__main__":
    init()


