#pyCheckSumCompare

This was a simple tool I created to help learn the simplicity and power of python. 

The problem it was created for was a team at work was setting up a new nexus repository in a new 
center in preparation for decommissioning the old data center.  Everything was good except for 
one application was failing to start up when deployed from the new nexus.   What they discovered
was that the application's md5 checksum file was different between the original nexus 
source and the new nexus - meaning the file was corrupted somehow during transfer or was mislabled/misnamed. 

This got me thinking that there could be other deployables with the same issue but we had
not found them yet.    

With a simple find/awk command I was able to create a command that would find all the md5 and create a 
file with file name and contents (the checksum).   Running this on both the original server
and new server gave us the list of files and checksums. 

Having the files we needed to see what the differences where.  I originally consider using
the comm command but that is comparing the entire line and we want to find the lines that have the
same content in the first column (filename) but different values in column 2. 

Another consideration is the contents of the file from the new server should be a subset of 
the file from the original nexus as old versions that were not deployed anymore were not 
copied over.   

## Generating the files

Using the find command I created a file with the sha1 files from my .m2 directory.  And then
as a test I made a copy of that file and added a line and modified a checksum to 
verify that the application worked. 

    find . -name "*.sha1" | awk '{printf("%s ", $1); system("cat " $1); printf("\n")}' > ~/temp/ctxfiles.txt
    
I later used the application to find differences in a directory of files between two computers.  
For that I generated an actual file of checksums. 

    find . -type f -exec sum {} \; | awk '{print $3, $1}' > checksums.txt
    
## Running pyCheckSumCompare.py

    ./pyCheckSumCompare.py -h
    usage: pyCheckSumCompare.py [-h] [-s SOURCEFILENAME] [-c SUBSETFILENAME]
                                [--version]

    check the contents of two files containing lists of checksums for differences

    optional arguments:
      -h, --help         show this help message and exit
      -s SOURCEFILENAME  Contains the largest(Superset) list of files with
                         checksums.
      -c SUBSETFILENAME  File you wish to check values against source file.
      --version          show program's version number and exit