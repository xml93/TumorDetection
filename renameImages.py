import os

def main():
    dirName = "/images/"
    os.chdir(os.getcwd()+dirName)
    top = os.getcwd()
    for root, dirs, files in os.walk(top, topdown=False):
        for name in dirs:
            print(os.path.join(root, name))
        for name in files:
            if ("thumbnailViewer" in name and "images" not in name):
                if len(name) == 22:
                    print(name)
                    print(name.replace('thumbnailViewer-',''))
                    newFilename = os.path.join(root,name.replace('thumbnailViewer-',''))
                elif len(name) == 21 :
                    print(name)
                    print(name.replace('thumbnailViewer-','0'))
                    newFilename = os.path.join(root,name.replace('thumbnailViewer-','0'))
                print("---")
                filename = os.path.join(root, name)
                
                os.rename(filename, newFilename)
main()
