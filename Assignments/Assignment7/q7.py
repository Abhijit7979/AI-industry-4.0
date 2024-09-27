import numpy as np

def convolve2d(image, kernel):

    i_height, i_width = image.shape
    k_height, k_width = kernel.shape
    o_height = i_height - k_height + 1
    o_width = i_width - k_width + 1

    output = np.zeros((o_height, o_width))
  
    for i in range(o_height):
        for j in range(o_width):
            output[i, j] = np.sum(image[i:i+k_height, j:j+k_width] * kernel)
    return output

image = np.array([[0,0,0,0,0],
                  [1,1,1,1,1],
                  [0,0,0,0,0],
                  [0,0,0,0,0],
                  [0,0,0,0,0]])

filter = np.array([[1.5, -1.5],
                   [-1.5, 1.5]])

result = convolve2d(image, filter)

print("\nConvolution Result:")
print(result)

if np.all(result ==  0):
    print(" horizontal line  is present")
else :
    print(" horizontal line  is not present")
