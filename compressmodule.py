import zlib,base64

#Splitting code into functions
def compress(inputfile, outputfile):
    read_text = open(inputfile, 'r').read()
    changed_text = bytes(read_text,'utf-8')
    compressed_text= base64.b64encode(zlib.compress(changed_text,9))

    decoded_text = compressed_text.decode('utf-8')

    new_text = open(outputfile, 'w')
    new_text.write(decoded_text)


def decompress(inputfile, outputfile):
    file_content = open(inputfile,'r').read()#The input file actually needs to be read from before any decompression can happen
    encoded_data =file_content.encode('utf-8')#It is then encoded from string
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompressed_data.decode('utf-8')
    file = open(outputfile, 'w')
    file.write(decoded_data)
    file.close()
