import click
import sys
import subprocess

def decode_line(line, encoding=sys.stdout.encoding):
    return line.decode(encoding)

def kdeconnect_fetch_ids():
    process = subprocess.Popen(["kdeconnect-cli", "-a", "--id-only"], stdout=subprocess.PIPE, shell=True)
    out = process.stdout.readlines()
    targets = []
    for line in out:
        id = decode_line(line).strip()
        targets.append(id)
    return targets

def targets_file_to_ids(path):
    file = open(path, "r")
    out = file.readlines()
    targets = []
    for line in out:
        id = line.strip()
        targets.append(id)
    return targets


@click.command()
@click.option('--message', '-m', default="ping", help="Message to be sent to all devices.")
@click.option('--targets', '-t', type=click.Path(exists=True), help="Optional text file containing all devices to ping.")
def ping(message, targets):
    targets = targets_file_to_ids(targets) if targets else kdeconnect_fetch_ids()
    print(targets)
    for target in targets:
        print( "## Sending command to device: " + str(target) )
        command = ['kdeconnect-cli', '--ping-msg', message, '-d', target]
        process = subprocess.Popen(" ".join(command), stdout=subprocess.PIPE, shell=True)

