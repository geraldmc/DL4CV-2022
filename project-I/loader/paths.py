import os
'''
Adapted from https://github.com/PyImageSearch/imutils
'''

image_types = (".ppm", ".jpeg", ".png", ".tif", ".tiff")

def list_images(base_path, contains=None):
    # return the set of files that are valid
    return list_files(base_path, valid_extension=image_types, contains=contains)


def list_files(base_path, valid_extension=None, contains=None):
    # loop over the directory structure
    for (root, dir_names, filenames) in os.walk(base_path):
        # loop over the filenames in the current directory
        for filename in filenames:
            # if the contains string is not none and the filename does not contain
            # the supplied string, then ignore the file
            if contains is not None and filename.find(contains) == -1:
                continue

            # determine the file extension of the current file
            ext = filename[filename.rfind("."):].lower()

            # check to see if the file is an image and should be processed
            if valid_extension is None or ext.endswith(valid_extension):
                # construct the path to the image and yield it
                image_path = os.path.join(root, filename)
                yield image_path