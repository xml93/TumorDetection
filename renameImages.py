import os

def main():
    dirName = "/images/"
    os.chdir(os.getcwd()+dirName)
    top = os.getcwd()
    for root, dirs, files in os.walk(top, topdown=False):
        for name in dirs:
            print(os.path.join(root, name))
        for name in files:
            filename = os.path.join(root, name)
            newFilename = os.path.join(root,name.replace('thumbnailViewer-',''))
            os.rename(filename, newFilename)
main()
