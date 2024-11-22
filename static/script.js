// Función para borrar el canvas
function clearCanvas() {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    context.clearRect(0, 0, canvas.width, canvas.height);
}

// Función para dibujar en el canvas
let drawing = false;
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

// Configuración del canvas para el dibujo
context.lineWidth = 10; // Ancho del trazo
context.lineCap = 'round'; // Bordes redondeados
context.strokeStyle = 'black'; // Color del trazo

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

function startDrawing(event) {
    drawing = true;
    context.beginPath();
    context.moveTo(event.offsetX, event.offsetY);
}

function draw(event) {
    if (!drawing) return;
    context.lineTo(event.offsetX, event.offsetY);
    context.stroke();
}

function stopDrawing() {
    drawing = false;
}

// Función para convertir el dibujo a base64
function getCanvasImage(canvas) {
    return canvas.toDataURL('image/png'); // Convierte el dibujo a una imagen en formato base64
}

// Función para predecir el número dibujado
async function predict() {
    const canvas = document.getElementById('canvas');
    const imageBase64 = getCanvasImage(canvas);
    const errorMessageElement = document.getElementById('error-message');
    errorMessageElement.innerHTML = ''; // Limpiar mensajes de error previos

    try {
        // Enviar la imagen al servidor
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: imageBase64.split(',')[1] }), // Enviar solo la parte de datos
        });

        const data = await response.json();
        const predictionElement = document.getElementById('prediction');

        if (data.prediction !== undefined) {
            predictionElement.innerHTML = `Predicción: <strong>${data.prediction}</strong>`;
        } else {
            predictionElement.innerHTML = 'Error al hacer la predicción';
        }
    } catch (error) {
        errorMessageElement.innerHTML = `Error en la solicitud: ${error.message}`;
    }
}
