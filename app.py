from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__, static_folder='static')  

model = load_model('modelo/mnist_model.h5')

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        img_data = request.get_json()
        img_base64 = img_data['image']

        
        img_bytes = base64.b64decode(img_base64)
        img = Image.open(BytesIO(img_bytes))

       
        img = img.convert('L').resize((28, 28))  
        img_array = np.array(img) / 255.0  
        img_array = np.reshape(img_array, (1, 28, 28, 1))  

      
        prediction = model.predict(img_array)
        predicted_digit = np.argmax(prediction)
        print(prediction)

        return jsonify({'prediction': int(predicted_digit)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
