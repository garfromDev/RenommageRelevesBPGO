# -*- coding: utf8 -*-

# entree : des fichiers de la forme : Relevé CB - 07419889682 - 28022020.pdf
# on veut : 2020 02 CB.pdf
# de la forme : Extrait de compte - 07419889682 - 28022020.pdf
# on veut : 2020 02.pdf

import os as os
import re


def main(path='.'):
    print(os.listdir(path))
    for f in os.listdir(path):
        date_regex = re.compile(r"[\d]*\.")
        date = re.search(date_regex, f).group()[:-1]
        prefix = date[4:8] + u" " + date[2:4]
        cb = u" CB" if 'CB' in f else u""
        new_name = u"%s%s.pdf" % (prefix, cb)
        print "renomme %s en %s" % (os.path.join(
            path, f), os.path.join(path, new_name))
        os.rename(os.path.join(path, f), os.path.join(path, new_name))


if __name__ == '__main__':
    main('.')
