# Duplicate image Finder

##### Version : V.2.0

Find duplicate images using hash keys.

#### Requirements:

- Python 3.x
- Imagehash >= 4.0
- Pillow >= 4.1.1

##### Steps before running the code

```bash
git clone https://github.com/ArunAniyan/siamese.git

```

##### Virtual Environment Setup

```bash
virtualenv myenv
. myenv/bin/activate
pip install -r requirements.txt
```

#### " Find the needle from the haystack"

Takes in a set of reference or training images from a single directory and searches same / similar images from another directory.

To run the code :

```bash
cd siamese/

python duplicate_finder.py -r <training_directory> -t <test_directory>
```

The results will be written to output.txt in the current directory.

Result format - <TrainImage.> , <Duplicates..,>

---

---

##### Author : Arun Aniyan

##### Contact : aka.bhagya@gmail.com

###### Last Update : 11-02-23
