import gradio as gr
from ultralytics import YOLO
import cv2
import tempfile
import os

# Carga del modelo
modelo = YOLO("best.pt")

def detectar_imagen(imagen):
    resultado = modelo(imagen)
    return resultado[0].plot()

def detectar_video(video):
    # Crea archivo temporal para guardar el resultado
    temp_input = video
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    cap = cv2.VideoCapture(temp_input)
    fps = cap.get(cv2.CAP_PROP_FPS)
    w  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    out = cv2.VideoWriter(temp_output.name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        resultados = modelo(frame)
        anotado = resultados[0].plot()
        out.write(anotado)
    
    cap.release()
    out.release()
    return temp_output.name

demo = gr.Interface(
    fn=lambda imagen_o_video: detectar_imagen(imagen_o_video) if imagen_o_video.endswith(('.png', '.jpg', '.jpeg')) else detectar_video(imagen_o_video),
    inputs=gr.File(label="Sube imagen (.jpg/.png) o vídeo (.mp4)"),
    outputs=gr.Image(type="filepath", label="Resultado")  # Para imagen
)

# Alternativa más elegante: pestañas separadas
with gr.Blocks() as app:
    gr.Markdown("# Mecalux Pallet Detection")
    gr.Markdown("Sube una imagen o vídeo para que el modelo pueda hacer predicciones.")

    with gr.Tab("📸 Imagen"):
        imagen_input = gr.Image(type="pil")
        imagen_output = gr.Image()
        imagen_btn = gr.Button("Detectar imagen")
        imagen_btn.click(fn=detectar_imagen, inputs=imagen_input, outputs=imagen_output)

    with gr.Tab("🎞️ Vídeo"):
        video_input = gr.Video()
        video_output = gr.Video()
        video_btn = gr.Button("Detectar vídeo")
        video_btn.click(fn=detectar_video, inputs=video_input, outputs=video_output)

app.launch()
