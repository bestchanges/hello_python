#!/usr/bin/env python3


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



if __name__ == "__main__":
    for fname in ['withBOM.ged', 'withoutBOM.ged']:
        print('=={}=='.format(fname))
        with open(fname, 'rb') as f:
            detect_bom(f)

