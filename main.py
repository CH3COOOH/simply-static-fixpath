# -*- coding: utf-8 -*-
import re
import os
import sys

def walk_dir(folder, filter_=None):
	fileLst = []
	for root, dirs, files in os.walk(folder):
		for f in files:
			ff = os.path.join(root, f)
			if filter_ == None:
				fileLst.append(ff)
			else:
				for t in filter_:
					if t in ff:
						fileLst.append(ff)
						break
	return fileLst

def contains_non_ascii(s):
	return bool(re.search(r'[^\x00-\x7F]', s))
	
def fix_gb18030(str_):
	if b'\xa2\xe3' in str_:
		return str_.encode('gb18030').replace(b'\xa2\xe3', b'\x80')
	return str_.encode('gb18030') + b'\xa1\xa1'

def rename(top, iswalk=False):
	if iswalk:
		dl = walk_dir(top)
	else:
		dl = os.listdir(top)
	for fn in dl:
		if contains_non_ascii(fn) == False:
			continue
		fp = os.path.join(top, fn)
		new_name = None
		try:
			new_name = fp.encode('gb18030').decode('utf8')
			os.rename(fp, new_name)
		except:
			try:
				b_fp2 = fix_gb18030(fp)
				new_name = b_fp2.decode('utf8')
				os.rename(fp, new_name)
			except:
				print(f"!!! Unable to rename path: {fp}")
				continue
		print(f"-> {new_name}")

if __name__ == '__main__':
	top = sys.argv[1]
	rename(top)

	for sub in ['author', 'category', 'tag']:
		rename(os.path.join(top, sub))

	for sub in [os.path.join('wp-content', 'uploads')]:
		rename(os.path.join(top, sub), iswalk=True)