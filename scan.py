#!/usr/bin/env python
import argparse, os, itertools, collections
from bs4 import BeautifulSoup


# By default, outputs just references to unique output files
# can also output all references

parser = argparse.ArgumentParser()
parser.add_argument('scan_path', nargs='?', default=os.getcwd(),
                    help='Path or file to scan, defaults to current dir')
parser.add_argument('-a', '--all', action='store_true',
                    help='Display all references to external assets')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Verbose output')
args = parser.parse_args()


found_assets = []

def scan_html(path):
    """
    Scans an HTML file using BeautifulSoup
    """
    EXCLUDE = ['#']

    with open(path) as f:
        file_contents = f.read()
    soup = BeautifulSoup(file_contents)

    def flatten_list(l):
        return list(itertools.chain(*l))

    def get_all_attrs_from_tags(attr, tags):
        all_tags = flatten_list([soup.find_all(tag)
                                 for tag in tags])
        all_attrs = map(lambda x: x.get(attr), all_tags)
        return all_attrs

    all_hrefs = get_all_attrs_from_tags('href', ['a', 'link'])
    all_srcs = get_all_attrs_from_tags('src', ['img', 'script'])

    all_assets = flatten_list([all_hrefs, all_srcs])
    all_assets_cleaned = filter(lambda x: x and x not in EXCLUDE, all_assets)

    return all_assets_cleaned


def scan_css(path):
    pass


# This is a list of known file extensions and 
# regex rules for matching external assets referenced therein
# e.g. in an html file there can be rel="" and href=""

FILE_PARSERS = {
    'html': scan_html,
    'htm': scan_html,
    'css': scan_css,
}

KNOWN_EXTENSIONS = FILE_PARSERS.keys()

def has_known_extension(path):
    return path.split('.')[-1] in KNOWN_EXTENSIONS

def run_parser(path):
    print 'Found %s' % path
    path_ext = path.split('.')[-1]
    file_assets = FILE_PARSERS[path_ext](path)
    found_assets.extend(file_assets)
    return file_assets


scan_path = args.scan_path

# Does the input file end in one of the known extensions?
if has_known_extension(scan_path):
    # Scan just this file
    run_parser(scan_path)

else:
    # Recursively scan the directory
    for root, dirs, files in os.walk(scan_path):
        if args.verbose:
            print 'Scanning %s' % root

        for filename in files:
            if has_known_extension(filename):
                run_parser(os.path.join(root, filename))


# Pull out those referenced by url and de-dup
local_assets_unique = set()
url_linked_assets = []
for asset in found_assets:
    # TODO: handle a static_url here
    if asset.startswith('http://') or asset.startswith('https://'):
        url_linked_assets.append(asset)
    else:
        local_assets_unique.add(asset)


# Check that files exist?
# try:
#    with open('filename'): pass
# except IOError:
#    print 'Oh dear.'


# Sort by extension and print
assets_by_ext = collections.defaultdict(list)
for asset in local_assets_unique:
    ext = asset.split('.')[-1]
    assets_by_ext[ext].append(asset)


from pprint import pprint
print '\nLocal assets:'
for ext in sorted(assets_by_ext):
    print '\n<%s> files' % ext
    for asset in sorted(assets_by_ext[ext]):
        print '\t%s' % asset

print '\nExternal assets linked by url:'
pprint(sorted(url_linked_assets))

print ''

