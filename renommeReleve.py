#!/usr/bin/python2
# -*- coding: utf8 -*-

# entree : des fichiers de la forme : Relevé CB - 07419889682 - 28022022.pdf
# on veut : 2020 02 Relevé CB.pdf
# de la forme : Extrait de compte - 07419889682 - 28022022.pdf
# on veut : 2020 02 Extrait de compte.pdf
# si la date est inférieure au 10 du mois, on prend le mois précédent, attention à gérer l'année si Janvier
# si la date est entre le 10 et le 20, on ajoute 15 apres le mois : 2020 02 15

import os as os
import re
import sys


def main(path):
    f = os.path.basename(path)
    if not os.path.dirname(path):
        path = os.path.join('.', path)
    fich.write("path : %s\nf: %s\n" % (str(path), str(f)))
    if not f:
        return 1
    date_regex = re.compile(r"[\d]*\.")
    dateG = re.search(date_regex, f)
    if not dateG or not dateG.group():
        return 1
    date = dateG.group()[:-1]
    if not date or len(date) < 3:
        return 1
    prefix = (date[4:8] + u" " + date[2:4]).replace('_', ' ')
    fich.write("prefix : %s\n" % prefix)
    cb = " CB" if 'CB' in f else u""
    fich.write("CB: %s\n" % cb)
    new_name = "%s%s.pdf" % (prefix, cb)
    fich.write("new name : %s\n" % new_name)
    # fich.write("renomme %s en %s\n" % (f, new_name))
    os.rename(path, os.path.join(os.path.dirname(path), new_name))
    fich.write("renomagge effectue\n")
    return os.path.join(os.path.dirname(path), new_name)


if __name__ == '__main__':
    fich = open("/Users/alistef/Documents/log.txt", 'a')
    fich.write("\n\nexecution en cours...\n")
    fich.write("argv : %s %s\n" % (len(sys.argv), str(sys.argv)))
    fich.write("repertoire %s\n" % os.getcwd())
    if len(sys.argv) >= 1:
        print("handling %s" % sys.argv[1])
        fich.write("handling " + str(sys.argv[1]) + "\n")
        main(sys.argv[1])
        fich.close()