import os
import numpy as np
from pathlib import Path
import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras import layers
from tensorflow.keras.models import Model, load_model 

os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

def CRNN( ImageFolderPath, ImageName ):
    
    # Pretained model path
    model_path = r"D:\\RPA_UiPath\\TensorFlow2 x CRNN x UiPath\\CRNN.h5"
           
    # Get list of all the captcha testing images
    data_dir = Path( ImageFolderPath )
    Image = list(map(str, list(data_dir.glob(ImageName)))) 
    
    # Mapping characters to integers
    Characters = {'0','1','2','3','4','5','6','7','8','9'}
    char_to_num = layers.experimental.preprocessing.StringLookup(
                          vocabulary=sorted(list(Characters)), num_oov_indices=0, mask_token=None )
    # Mapping integers back to original characters
    num_to_char = layers.experimental.preprocessing.StringLookup(
                          vocabulary=char_to_num.get_vocabulary(), mask_token=None, invert=True )  
    
    def encode_single_sample( img_path ): 
        # 1. Read image
        img = tf.io.read_file( img_path )     
        # 2. Decode and convert to grayscale
        img = tf.io.decode_png( img, channels=1 )
        # 3. Convert to float32 in [0, 1] range
        img = tf.image.convert_image_dtype( img, tf.float32 )
        # 4. Resize to the desired size
        img = tf.image.resize( img, [32,104] )
        # 5. Transpose the image because we want the time dimension to correspond to the width of the image, 
        #    i.e., shape = (img_weight,img_height,1).
        img = tf.transpose( img, perm=[1,0,2] )
        return { "image": img }
    
    # Create validation dataset object
    validation_dataset = tf.data.Dataset.from_tensor_slices( (np.array(Image)) ) 
    validation_dataset = ( validation_dataset.map(
                           encode_single_sample, num_parallel_calls=tf.data.experimental.AUTOTUNE
                           ).batch(1).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
                          )
    
    # Build an custom endpoint layer of the pretrained model.
    class CTCLayer( layers.Layer ):
        def __init__( self, name=None, **kwargs ):
            super().__init__( name=name )
            self.loss_fn = K.ctc_batch_cost

        def call( self, y_true, y_pred ):
            batch_len = tf.cast( tf.shape(y_true)[0], dtype='int64' )
            input_length = tf.cast( tf.shape(y_pred)[1], dtype='int64' )
            label_length = tf.cast( tf.shape(y_true)[1], dtype='int64' )
        
            input_length = input_length*tf.ones( shape=(batch_len,1), dtype='int64' )
            label_length = label_length*tf.ones( shape=(batch_len,1), dtype='int64' )

            loss = self.loss_fn( y_true, y_pred, input_length, label_length )
            self.add_loss(loss)

            return y_pred
    
    model = load_model( model_path, custom_objects={'CTCLayer': CTCLayer} )

    # Get the prediction model by extracting layers till the output layer
    prediction_model = Model( model.get_layer( name='Input' ).input, model.get_layer( name='Softmax' ).output, name='Prediction' )
    
    # A utility function to decode the output of the network
    def decode_batch_predictions( pred ):
        input_len = np.ones(pred.shape[0]) * pred.shape[1]
        # Use greedy search. For complex tasks, you can use beam search
        results = K.ctc_decode( pred, input_length=input_len, greedy=True )[0][0][:,:4]
        # Iterate over the results and get back the text
        output_text = []
        for res in results:
            res = tf.strings.reduce_join(num_to_char(res)).numpy().decode('utf-8')
            output_text.append(res)
        return output_text    
    
    for batch in validation_dataset.take(1):
        batch_image = batch['image']
        pred = prediction_model.predict(batch_image)
        pred_text = decode_batch_predictions(pred)
    
    return pred_text[0]