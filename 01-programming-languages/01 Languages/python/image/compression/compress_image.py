if __name__ == "__main__":
    import argparse
    myparser = argparse.ArgumentParser()
    myparser.add_argument("-f", "--filename", required=True, help="Image's filename in current path to compress.")
    args = myparser.parse_args()

if args.filename is not None:
    print(f"Loading '{args.filename}' file...")

    import PIL.Image as Image
    import cloudpickle
    import os

    im = Image.open(args.filename)

    print("Current file:")
    print("-"*20)
    print(f"File size {os.stat(args.filename).st_size:,} Kb.")
    x, y = im.size
    print("Resolution: ", x, "x", y)
    print("File type: ", im.format_description)

    # Compress file
    # imc = im.resize((im.width, im.height),Image.ANTIALIAS)
    # imc = im.resize((int(im.width * 0.5), int(im.height * 0.5)), Image.Resampling.LANCZOS)

    set_quality = int(input("Set cuality for output image [5-95]: "))
    imc = im.resize((int(im.width * 1), int(im.height * 1)), Image.Resampling.LANCZOS)
    imc.save(f"{'Compressed_' + args.filename[2:]}", quality=set_quality, optimize=True);


    print("")
    print("Compresed file:")
    print("-"*20)
    newfile = "Compressed_" + args.filename[2:]
    new_im = Image.open(newfile)
    print(f"File size {os.stat(newfile).st_size:,} Kb.")
    x, y = new_im.size
    print("Resolution: ", x, "x", y)
    print("File type: ", new_im.format_description)
