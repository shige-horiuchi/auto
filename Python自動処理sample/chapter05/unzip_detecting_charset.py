import chardet
import os
import sys
import zipfile

def detect_filename(original_filename):
    guess_charset = chardet.detect(original_filename).get('encoding')
    if guess_charset is None:
        print(f'文字コードを推測できません')
        return original_filename.decode('cp437')
    else:
        print(f'推測された文字コード: {guess_charset}')
        return original_filename.decode(guess_charset)

def get_filename(info, charset):
    if info.flag_bits & 0x800:
        print(f'ファイル名はUTF-8でエンコードされています')
        filename = info.filename
    else:
        print(f'ファイル名はCP437または他の文字コードでエンコードされています')
        original_filename = info.filename.encode('cp437')
        if charset is None:
            filename = detect_filename(original_filename)
        else:
            print(f'指定した文字コード: {charset}')
            filename = original_filename.decode(charset)
    return filename

charset = None
path = None

if len(sys.argv) == 2:
    path = sys.argv[1]
elif len(sys.argv) >= 3:
    path, charset = sys.argv[1:3]
else:
    print(f'zipファイルを指定してください')
    sys.exit(0)

with zipfile.ZipFile(path, 'r') as zf:
    for info in zf.filelist:
        filename = get_filename(info, charset)
        print(f' - ファイル名: {filename}')

        if '/' in filename:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        if not os.path.isdir(filename):
            with open(filename, 'wb') as wf:
                wf.write(zf.read(info.filename))
