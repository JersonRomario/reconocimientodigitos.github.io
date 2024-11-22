import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Cargar el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocesamiento de datos
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))  # Redimensionar a 28x28x1
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))  # Redimensionar a 28x28x1

train_images, test_images = train_images / 255.0, test_images / 255.0  # Normalizar los datos

# Convertir las etiquetas a formato categórico (one-hot encoding)
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Crear el modelo
model = models.Sequential()

# Capa 1: Convolucional + MaxPooling
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# Capa 2: Convolucional + MaxPooling
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Capa 3: Convolucional
model.add(layers.Conv2D(128, (3, 3), activation='relu'))

# Capa Flatten
model.add(layers.Flatten())

# Capa densa (Fully Connected)
model.add(layers.Dense(128, activation='relu'))

# Capa de salida (Softmax para clasificación de 10 clases)
model.add(layers.Dense(10, activation='softmax'))

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(train_images, train_labels, epochs=20, batch_size=64, validation_data=(test_images, test_labels))

# Evaluar el modelo
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc}")

# Guardar el modelo entrenado
model.save('modelo/mnist_model.h5')

# Para hacer predicciones
# predictions = model.predict(test_images)
# predicted_class = np.argmax(predictions, axis=1)
