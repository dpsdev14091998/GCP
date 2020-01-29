from google.cloud import storage
import os


fld1 = 'folder1'
fld2= 'new'

os.mkdir(fld2)



sclient = storage.Client()
sbucket = sclient.get_bucket("ad-bucket2")
blobs = sbucket.list_blobs()
for b in blobs:
    fldr = fld2 + '/'
    if b.name.startswith(fld1) and b.name[-1] != '/':
        flder_strct = b.name.split('/')
        for folder in flder_strct[:-1]:
            fldr += folder + '/'
            try:
                os.mkdir(fldr)
            except Exception as e:
                pass
            
        b.download_to_filename(fldr + flder_strct[-1])

print('Bucket "folder1" has been replicated!')