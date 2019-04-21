#!/usr/bin/env python3

""" Задача - записать выходной файл в том же формате, что и входной.
То есть может быть
* BOM (byte order marker) в разных вариантах, или отсутствовать
   - надо в точности в выходной файл также записать BOM или без такового
* могут быть отличия в самом тексте

PS Первая строка, по-факту, не меняется, выглядит как "0 HEAD" но это не критерий
"""

def detect_bom( in_file):
    """
      BOM - byte order marker - may be in the very beginning of file
      if BOM is detected - save it for further writing into out_file to keep as is.

      @:param in_file
      @:type FILE - input
    """
    bom = None
    line = in_file.read(2)
    if not line:
        print("error reading")
        return

    if line == b"\xef\xbb":  # UTF-8
        bom = line + in_file.read(1)  # one more byte "\xbf"
        print("BOM detected: UTF-8")
    elif line == b"\xfe\xff" or line == b"\xff\xfe":
        bom = line
        print("BOM detected: UTF-16 (BE) or UTF-16 (LE)")
    else:
        in_file.seek(0)
        print("not detected any BOM. or other unsupported cases of BOM value")
    return bom


if __name__ == "__main__":
    for fname in ['withBOM.ged', 'withoutBOM.ged']:
        print('=={}=='.format(fname))
        with open(fname, 'rb') as infile:
            pass
            #  ## Old - ugly - WORKING code
            # bom = detect_bom(infile)
            # with open(fname + "__OUT.ged", "wb") as outfile:
            #     if bom:
            #         outfile.write(bom)
            #     for line in infile:
            #         outfile.write(line)

            # =================
            # binary file in, decode
            # text file out
            # Does not work - saves without BOM regardless input bom
            #
            # with open(fname + "__OUT.ged", "wt") as outfile:
            #     for line in infile:
            #         s = line.decode('utf-8-sig')
            #         print(s)
            #         outfile.write(s)

            # =================
            # binary file in, decode,  binary file out
            # Does not work: Looks like it writes bom into each line
            with open(fname + "__OUT.ged", "wb") as outfile:
                for line in infile:
                    s = line.decode('utf-8-sig')
                    print(s.strip())
                    outfile.write(s.encode('utf-8-sig'))



