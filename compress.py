#File Compression and Encoding in Python

import zlib, base64#These are the two imports that are used. zlib deals with the compression of files, while base64 deals with the encoding of files. 
read_text = open('practice.txt', 'r').read()#This function is used in order to read the file.
# print(read_text)
changed_text = bytes(read_text,'utf-8')#The z-lib.compress() function only takes a byte value, not a string. So this 'bytes function is used as a way to convert the string into bytes. The utf-8 function is the string format that would be converted. 
compressed_text= base64.b64encode(zlib.compress(changed_text, 9))#This is used to encode the text into base 64 and the value of 9 represents the highest level of compression that is going to be used. 

decoded_text = compressed_text.decode('utf-8')# This is used to decode the encoded data that has been encoded and compressed so it can be written to the new file. 

new_text = open('newtext.txt', 'w')# This is to create a new text file which the decoded file would be written to. It is decoded and not encoded, becuase the file can only be written to the value of strings. So it would require a decoding before it can be written to. 
new_text.write(decoded_text)#Writes the old file into the new one. 
# print(compressed_text)

#File Decompression
decompressed_data = zlib.decompress(base64.b64decode(compressed_text))#This is used for decompression of a compressed file. The file is still encoded with the b64encode() function, so it would need to be decoded before it is decompresssed. 
# print(decompressed_data)






