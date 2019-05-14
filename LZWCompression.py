from sys import argv
import string
from PIL import Image, TiffImagePlugin
from io import BytesIO
import base64

def doCompress(file_name, ext):
    undefinedExt = True

    ##JIKA FILE TEXT
    if ext == "txt":
        undefinedExt = False

        input_file = open(file_name)
        data = input_file.read()[:-1]
        input_file.close()

    ##JIKA FILE TIFF
    elif ext == "tif" or ext == "tiff":
        undefinedExt = False

        ##UBAH DATA GAMBAR MENJADI BASE64 -> STRING
        img = Image.open(file_name)
        img_buffer = BytesIO()
        img.save(img_buffer, format="TIFF")
        data = base64.b64encode(img_buffer.getvalue())
        data = str(data)

    ##JIKA FILE GIF
    elif ext == "gif":
        undefinedExt = False

        ##UBAH DATA GAMBAR MENJADI BASE64 -> STRING
        img = Image.open(file_name)
        img_buffer = BytesIO()
        img.save(img_buffer, format="GIF")
        data = base64.b64encode(img_buffer.getvalue())
        data = str(data)

    ##JIKA EXTENSI TIDAK TERDEFINISI
    elif undefinedExt:
        print("[ERROR] : Undefined file extension")
        return -1
    
    ##MULAI COMPRESSION
    dictionary = dict()
    output = ""
    p = str(data[0])
    i = 1
    count = 0

    for char in string.digits+string.ascii_letters+string.punctuation+string.whitespace:
        dictionary[char] = count
        count += 1

    while i != len(data):
        c = str(data[i])
        
        if p+c in dictionary:
            p += c
            
        else:
            output += str(dictionary[p]) + "."
            dictionary[p+c] = len(dictionary)
            p = c

        i += 1
    
    output += str(dictionary[p])

    ##MENULIS HASIL COMPRESSION KE FILE TEXT
    output_file = open(file_name.split(".")[0]+".txt", "w")
    if ext == 'txt':
        output_file.write("TEXT " + output)
    elif ext == 'tif' or ext == 'tiff':
        output_file.write("TIFF " + output)
    elif ext == 'gif':
        output_file.write("GIF " + output)
    output_file.close()
    

def doDecompress(file_name, ext):
    ##FILE TERKOMPRESS SELALU BERTIPE TEXT
    if ext == "txt":
        input_file = open(file_name)
        data = input_file.read()
        input_file.close()

        ##AMBIL TIPE FILE DAN DATA
        file_type = data.split(' ')[0]
        data = data.split(' ')[1]

        ##MULAI DEKOMPRESI
        dictionary = dict()
        output = ""
        count = 0

        for char in string.digits+string.ascii_letters+string.punctuation+string.whitespace:
            dictionary[count] = char
            count += 1

        ##SPLIT DATA SESUAI INDEKSNYA
        data = [int(i) for i in data.split(".")]

        cw = data[0]
        output += dictionary[cw]
        pw = cw

        for code in data[1:]:

            if code in dictionary:
                output += dictionary[code]
                p = dictionary[pw]
                c = dictionary[code][:1]

                dictionary[count] = p+c
                count += 1
            else:
                p = dictionary[pw]
                c = p[:1]

                output += p+c
                dictionary[count] = p+c
                count += 1

            pw = code

        ##JIKA TIPE FILE YANG AKAN DIKOMPRES FILE TEXT
        if file_type == "TEXT":
            output_file = open(file_name.split(".")[0]+".txt", "w")
            output_file.write(output)
            output_file.close()

        ##JIKA TIPE FILE YANG AKAN DIKOMPRES FILE TIFF
        elif file_type == "TIFF":
            output = base64.b64decode(output[2:-1])
            img_buffer = BytesIO(output)
            img = Image.open(img_buffer)
            img.save(file_name.split(".")[0]+".tiff")

        ##JIKA TIPE FILE YANG AKAN DIKOMPRES FILE GIF
        elif file_type == "GIF":
            output = base64.b64decode(output[2:-1])
            img_buffer = BytesIO(output)
            img = Image.open(img_buffer)
            img.save(file_name.split(".")[0]+".gif")
            
    else:
        print("[ERROR] : Undefined file extension")

def main():
    if len(argv) == 3:
        try:
            option = argv[1]
            file_name = argv[2]
            extension = file_name.split(".")[1]

            if option == "compress":
                doCompress(file_name, extension)
            elif option == "decompress":
                doDecompress(file_name, extension)
            else:
                print("[ERROR] : Undefined option (compress/decompress)")
        except(FileNotFoundError):
            print("[ERROR] : No such file is found")
        
        
    else:
        print("[ERROR] : Number of argument didn't match")
        print("[USAGE] : python main [compress|decompress] <file_name>.<file_extension>")

if __name__ == "__main__":
    main()