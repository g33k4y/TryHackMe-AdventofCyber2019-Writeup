import os, zipfile, exiftool

#zipfile library example
#for Question 1
with zipfile.ZipFile('final-final-compressed.zip', 'r') as zip_ref:
  zip_ref.extractall('extracted/')
  c = zip_ref.namelist()
  for a in c:
    zname = 'extracted/'+a
    fname = 'files/'
    with zipfile.ZipFile(zname, 'r') as zip_refa:
      zip_refa.extractall(fname)

#os lib example
listFiles = os.listdir('files/')
print(f"Number of non-zip files: {len(listFiles)}")


#exiftool library example
#for Question 2
with exiftool.ExifTool() as et:
	listFilesMeta = et.execute_json("files/")

countFiles = 0
for fileMeta in listFilesMeta:
	if (1.1 in list(fileMeta.values())):
		print(f"File containing Version 1.1: {fileMeta['File:FileName']}")
		countFiles+=1
print(f"Number of Files containing Version 1.1: {countFiles}")



#for Question 3
for zfile in listFiles:
	zpath=str(fname)+str(zfile)
		
	with open(zpath, errors='ignore') as read:
		passage = read.readlines()
		for line in passage:
			if ('password' in line):
				print(f"Password found in this line: {line.strip()}")
				print(f"Path that contains password: {zfile}")

