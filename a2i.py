import numpy as np
from math import sqrt, ceil
import cv2
#ref: https://stackoverflow.com/questions/60193896/convert-file-into-grayscale-image
def convert_apk_to_img(input_file, output_filename):
    #Input file name (random file I found in my folder).
    input_file_name = input_file

    #Read the whole file to data
    with open(input_file_name, 'rb') as binary_file:        
        data = binary_file.read()

    # Data length in bytes
    data_len = len(data)

    # d is a verctor of data_len bytes
    d = np.frombuffer(data, dtype=np.uint8)

    # Assume image shape should be close to square
    sqrt_len = int(ceil(sqrt(data_len)))  # Compute square toot and round up

    # Requiered length in bytes.
    new_len = sqrt_len*sqrt_len

    # Number of bytes to pad (need to add zeros to the end of d)
    pad_len = new_len - data_len

    # Pad d with zeros at the end.
    # padded_d = np.pad(d, (0, pad_len))
    padded_d = np.hstack((d, np.zeros(pad_len, np.uint8)))

    # Reshape 1D array into 2D array with sqrt_len pad_len x sqrt_len (im is going to be a Grayscale image).
    im = np.reshape(padded_d, (sqrt_len, sqrt_len))

    # Save image
    cv2.imwrite(output_filename, im)
    return None
    # Display image
    #cv2.imshow('im' ,im)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


