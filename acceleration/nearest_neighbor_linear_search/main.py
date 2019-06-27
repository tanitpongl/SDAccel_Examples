from keras.models import Model
from keras.layers import Add, Activation, Concatenate, Conv2D, Dropout
from keras.layers import Flatten, Input, GlobalAveragePooling2D, MaxPooling2D
import keras.backend as K
import tensorflow as tf
import random as rand
import numpy as np
import pathlib
import IPython.display as display
import PIL
from keras.preprocessing.image import img_to_array, array_to_img, load_img


image_path = "data/imagenet/"
fifo_name = 'fifo_first_layer'



n = 224
c = 3
input_data_random = np.array([[[[1for j in range(c)] for i in range(n)] for k in range(n)]])
weight_data_random = np.array([[[[1 for j in range(96)] for i in range(3)] for k in range(7)] for l in range(7)])
bias_data_random = np.array([1 for j in range(96)])

input_shape = (224,224,3)
input_img = Input(shape=input_shape)

conv1 = Conv2D(96, (7,7), activation='relu', strides=(2,2), padding='same', name='conv1',weights=[weight_data_random,bias_data_random])(input_img)

model_input = Model(inputs = input_img,outputs = conv1)
#model_input.summary()




# ----------- oading an image with the Keras API
from keras.preprocessing.image import load_img
img = load_img(image_path + "cat.jpg")
# report details about the image
print("--- Input image details ---")
print(type(img))
print(img.format)
print(img.mode)
print(img.size)
# show the image
#img.show()
img = img.resize(size=(224,224))
x = img_to_array(img)
x = x.reshape((1,224,224,3))

# -------- start first layer prediction
first_layer_output = model_input.predict(np.array(x));
print(first_layer_output)
#first_layer_output_img = array_to_img(first_layer_output[:,:,:,:3].reshape(112,112,3))
#first_layer_output_img.show()

# --------- test piping
import subprocess
import sys
import os
#os.environ[XCL_EMULATION_MODE]="sw_emu"
my_env = os.environ.copy()
'''proc = subprocess.Popen("./nearest",
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    env=my_env)
'''
proc = subprocess.Popen("./test/test",
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    env=my_env)
print("start sending data")
while True:
  line = proc.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  print( "test:", line.rstrip())
'''
#np.savetxt(proc.stdin, first_layer_output.flatten(), delimiter=' ',fmt ='%f')
testarray = np.array([1.2,23.2,1.2,3331.1,23.2,0.1])
np.savetxt(proc.stdin, testarray.flatten(), delimiter=' ',fmt ='%f')
proc.stdin.write("end".encode("ascii"))
print("finish sending data")
proc.stdin.close()
result = proc.stdout.readline()
print("result back =",result.decode("ascii"))
while True:
  line = proc.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  print( "test:", line.rstrip())
'''


#output = proc.communicate("output_to_exec".encode("ascii"))[0]
#print(output.decode("ascii"))
#proc.stdin.flush()
#result = proc.stdout.readline().strip()
#print(result)
