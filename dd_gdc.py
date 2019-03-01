import sys
import os

DATA = sys.argv[1]
EXT = sys.argv[2]
NUMBER_FILES = int(sys.argv[3])


def get_mafs(data_dir, ext):
    maf_files = []
    for path, subdirectories, files in os.walk(data_dir):
        maf_files = maf_files + [os.path.join(path, maf) for maf in files if maf.endswith(ext)]
    return maf_files[0:NUMBER_FILES]


def move_mafs(maf_files):
    if "out_dir" in os.listdir():
        for file in maf_files:
            os.system(f"cp {file} out_dir")
    else:
        os.mkdir("out_dir")
        for file in maf_files:
            os.system(f"cp {file} out_dir")
    for path, subdir, files in os.walk("out_dir"):
        zip_mafs = [os.path.join(path, maf) for maf in files if maf.endswith("maf.gz")]
        print(zip_mafs)
        for zip_file in zip_mafs:
            print(zip_file)
            os.system(f"gunzip {zip_file}")


def main():
    maf_files = get_mafs(data_dir=DATA, ext=EXT)
    move_mafs(maf_files)


if __name__ == '__main__':
    main()
