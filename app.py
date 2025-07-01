from PIL import Image, ImageDraw
import gradio as gr
from ultralytics import YOLO
import cv2
import tempfile
import os
import numpy as np

# Carga del modelo
modelo = YOLO("best.pt")

def detectar_imagen(imagen):
    if imagen is None:
        img = Image.new("RGB", (512, 200), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text((20, 80), "⚠️ Sube una imagen primero", fill=(0, 0, 0))
        return img
    resultado = modelo(imagen)
    return resultado[0].plot()

def detectar_video(video):
    if video is None:
        temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        frame = Image.new("RGB", (640, 360), color=(255, 255, 255))
        draw = ImageDraw.Draw(frame)
        draw.text((120, 150), "⚠️ Sube un video primero", fill=(0, 0, 0))
        frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        out = cv2.VideoWriter(temp_output.name, cv2.VideoWriter_fourcc(*'mp4v'), 1, (640, 360))
        out.write(frame)
        out.release()
        return temp_output.name

    temp_input = video
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    cap = cv2.VideoCapture(temp_input)
    fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

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

with gr.Blocks() as app:
    gr.Markdown("# Mecalux Pallet Detection")
    gr.Markdown("Sube una imagen o vídeo para que el modelo pueda hacer predicciones.")

    with gr.Tab("Imagen"):
        imagen_input = gr.Image(type="pil")
        imagen_output = gr.Image()
        imagen_btn = gr.Button("Detectar imagen")
        imagen_btn.click(fn=detectar_imagen, inputs=imagen_input, outputs=imagen_output)

    with gr.Tab("Vídeo"):
        video_input = gr.Video()
        video_output = gr.Video()
        video_btn = gr.Button("Detectar vídeo")
        video_btn.click(fn=detectar_video, inputs=video_input, outputs=video_output)

app.launch()

