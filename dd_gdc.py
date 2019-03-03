import sys
import os

DATA = sys.argv[1]  #
EXT = sys.argv[2]
NUMBER_FILES = sys.argv[3]
OUT = sys.argv[4]


def get_mafs(data_dir, ext):
    maf_files = []
    for path, subdirectories, files in os.walk(data_dir):
        maf_files = maf_files + [os.path.join(path, maf) for maf in files if maf.endswith(ext)]
    if NUMBER_FILES != 'all':
        maf_files = maf_files[0:int(NUMBER_FILES)]
    return maf_files


def move_mafs(maf_files):
    if OUT in os.listdir():
        for file in maf_files:
            os.system(f"cp {file} {OUT}")
    else:
        os.mkdir(OUT)
        for file in maf_files:
            os.system(f"cp {file} {OUT}")
    for path, subdir, files in os.walk(OUT):
        zip_mafs = [os.path.join(path, maf) for maf in files if maf.endswith("maf.gz")]
        print(zip_mafs)
        for zip_file in zip_mafs:
            print(zip_file)
            os.system(f"gunzip {zip_file}")
            try:
                os.system("python delmh/vci2mh.py --vci-type g --vci-s " + zip_file.replace(".maf.gz", ".maf") +
                          " --ref-fa hg/hg38.fa --o-func-str " + "\"lambda vci_path: os.path.splitext(vci_path)["
                                                                     "0].replace('mutect_maf', 'mutect_o') + "
                                                                     "args.o_suf\"")
                os.system(f"rm {zip_file.replace('.maf.gz', '.maf')}")
            except NameError:
                print("NameError issue in processing!")


def main():
    maf_files = get_mafs(data_dir=DATA, ext=EXT)
    move_mafs(maf_files)


if __name__ == '__main__':
    main()
