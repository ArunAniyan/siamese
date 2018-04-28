from __future__ import print_function

"""
Solution for SARAO Data Science Technical Challenge
===================================================

Author        : Arun Aniyan
Institution   : SKA SA/ RATT
Contact       : aka.bhagya@gmail.com
Date          : 24-04-18
Version       : V.1.0
Compatibility : Python 2.7 & 3

" Find the needle from the haystack"

Takes in a set of reference or training images from a single
directory and searches same / similar images from another directory.

To run the code :

python duplicate_finder.py -r <training_directory> -t <test_directory>

The results will be written to output.txt in the current directory.

Result format : <Test Image>, <Duplicates..,>

Requirements:
* Imagehash == 4.0
* Pillow == 4.1.1


"""


""" Imports """

import argparse
from time import time
import imagehash
from PIL import Image
import os

""" Useful Functions """


# Traverse Directory and get list of files
def traverse_dir(dirname):
    fl_list = []
    for filename in os.listdir(dirname):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            fl_list.append(filename)
        else:
            continue
    return fl_list


""" Extract pHash and dHash for images"""

# Hasher function
def hasher(basedir, files):
    pdb = {}
    ddb = {}
    pdb = pdb.fromkeys(files)
    ddb = ddb.fromkeys(files)
    for infile in list(pdb.keys()):
        try:
            pdb[infile] = imagehash.phash(Image.open(os.path.join(basedir, infile)))  # pHash
            ddb[infile] = imagehash.dhash(Image.open(os.path.join(basedir, infile)))  # dHash
        except:
            print (('Error with file %s in %s')%(infile,basedir))

    return pdb, ddb


# Map filenames from hashcode
def find_key(dic, val):
    return [x for x in list(dic.keys()) if dic[x] == val]


# Find duplicates and originals
def find_duplicates(traindb, testdb):
    # Compare dicts
    shared_items = set(traindb.values()) & set(testdb.values())
    shared_items = [x for x in iter(shared_items)]  # Convert set to list
    # Get Originals
    originals = [find_key(traindb, item) for item in shared_items]
    # Find duplicates
    duplicates = [find_key(testdb, item) for item in shared_items]
    return originals, duplicates


# Pretty Reformating - Remove unwanted characters from list
def reformat(reflist, duplist):
    l = reflist + ' ' + str(duplist)
    l = l.replace('[', '')
    l = l.replace(']', '')
    l = l.replace("'", '')
    l = l.replace(",", '')
    l = l.replace(" ", ',')
    return l


""" Main """

if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-r", "--train_directory", required=True, help="Location of reference / train images")
    ap.add_argument("-t", "--test_directory", required=True, help="Location of test images")
    args = vars(ap.parse_args())

    refdir = args['train_directory']
    testdir = args['test_directory']

    start_time = time() # Start time for calculations

    # Get file list
    ref_files = traverse_dir(refdir)
    test_files = traverse_dir(testdir)

    # Get hashes for test and train
    ref_pdb, ref_ddb = hasher(refdir, ref_files)
    test_pdb, test_ddb = hasher(testdir, test_files)

    # Find duplicates and originals from hashcode
    p_originals, p_duplicates = find_duplicates(ref_pdb, test_pdb)
    d_originals, d_duplicates = find_duplicates(ref_ddb, test_ddb)

    # Exit of no copies are found
    if (len(p_originals) == 0) or (len(d_originals) == 0):
        print('No duplicates found...')
        print(('Search Time was %f seconds') % (time() - start_time))
        exit(0)


    # Names of unique originals
    originals = p_originals or d_originals
    originals = [str(i[0]) for i in originals]

    # Name of unique duplicate files
    duplicates = p_duplicates or d_duplicates

    end_time = time() # End time for calculations

    # Save results to output.txt
    for i in range(0, len(originals)):
        text = reformat(originals[i], duplicates[i])
        with open("output.txt", "a") as text_file:
            text_file.write(text + '\n')

    print(('Took %f seconds for search.') %(end_time - start_time))
    print(('Found duplicates for %d images.') %(len(originals)))
    print('Result written to output.txt')



