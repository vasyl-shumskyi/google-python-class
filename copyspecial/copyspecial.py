#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

#dir = sys.argv[1]
#files = os.listdir(dir)
#for file in files: print os.path.abspath(file)


def list_files(dir): 
#  dir = sys.argv[-1]
  list_f = []
  filesss = os.listdir(dir)
  for filename in filesss: 
    file__name = re.findall(r'__\w+__',filename)
    if file__name: list_f.append(os.path.abspath(os.path.join(dir, filename)))
  return list_f  


def copy_files(fffiles, newdir):
  if not os.path.exists(newdir): os.mkdir(newdir)
  for fname in fffiles: 
    print 'Copying', fname, '-->', newdir, '\n',
    shutil.copy(fname,newdir)


def zip_files(fillles, archive): 
    cmd = 'zip ' + archive + ' ' + ' '.join(fillles)
    print "\nCommand to run:\n", cmd, '\n'  
    (status, output) = commands.getstatusoutput(cmd)
    if status: 
      sys.stderr.write(output)
      sys.exit(1)
    print output  



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions

  files = []
  for dddir in args: files.extend(list_files(dddir))
 
  if todir: copy_files(files, todir)
  elif tozip: zip_files(files, tozip)
  else: print '\n'.join(files)




  
if __name__ == "__main__":
  main()
