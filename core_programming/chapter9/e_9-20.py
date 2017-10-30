# GZip
import gzip
f_in = open('ReadMe.txt', 'rb')
f_out = gzip.open('ReadMe.txt.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()

f = gzip.open('ReadMe.txt.gz', 'rb')
f_out = open('ReadMe3.txt', 'wb')
file_content = f.read()
f_out.write(file_content)
f.close()
f_out.close()
