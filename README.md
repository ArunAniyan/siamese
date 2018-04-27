# Duplicate image Finder

Find duplicate images using hash keys. 


##### Author        : Arun Aniyan

##### Institution   : Rhodes University

##### Contact       : aka.bhagya@gmail.com

##### Date          : 24-04-18

##### Version       : V.1.0

##### Compatibility : Python 2.7 & 3

#### " Find the needle from the haystack"

Takes in a set of reference or training images from a single directory and searches same / similar images from another directory.

To run the code :
```
python duplicate_finder.py -r <training_directory> -t <test_directory>
```
The results will be written to output.txt in the current directory.

Result format -  <TestImage.> , <Duplicates..,>

Requirements:
* (Imagehash)[https://pypi.org/project/ImageHash/] == 4.0
* Pillow == 4.1.1
