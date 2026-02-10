# Sistema de Visión por Computador para Inspección Automática de Palets

## Descripción general
Este proyecto consiste en el desarrollo de un sistema de **visión por computador basado en Deep Learning** para la **inspección automática de palets y paquetes en entornos logísticos**, con el objetivo de detectar defectos, errores de embalaje y anomalías dimensionales durante el proceso de recepción de mercancía.

El proyecto ha sido desarrollado en el marco del **Mecalux AI Challenge** organizado por la **Universitat Politècnica de Catalunya (UPC)**, abordando un problema real de entorno industrial donde la automatización y la fiabilidad del sistema son factores clave.

---

## Objetivo
El objetivo principal es diseñar y entrenar un modelo de **detección de objetos** capaz de identificar y clasificar correctamente el estado de palets y paquetes en tiempo real, reduciendo la dependencia de inspecciones manuales y mejorando la eficiencia del proceso logístico.

El sistema debe ser capaz de detectar las siguientes seis clases:

- Palet roto  
- Palet en buen estado  
- Paquete con embalaje correcto y dimensiones correctas  
- Paquete con embalaje correcto y dimensiones incorrectas  
- Paquete con embalaje incorrecto y dimensiones correctas  
- Paquete con embalaje incorrecto y dimensiones incorrectas  

---

## Dataset
Para este proyecto se creó un **dataset propio** a partir de imágenes reales de entornos logísticos.

Características del dataset:
- Imágenes reales etiquetadas manualmente: 850  
- Número de clases: 6  
- Etiquetado manual imagen a imagen  

Con el objetivo de mejorar la robustez y capacidad de generalización del modelo, el dataset fue ampliado hasta **2.500 imágenes** mediante técnicas de **data augmentation**, incluyendo:
- Rotaciones
- Recortes
- Adición de ruido
- Variaciones geométricas y de iluminación

Las tareas de anotación y aumento de datos se realizaron utilizando la herramienta **Roboflow**.

---

## Arquitectura del modelo
El sistema se basa en un modelo de **detección de objetos YOLOv11x**, una arquitectura diseñada para ofrecer un alto rendimiento en tareas de detección en tiempo real.

Principales características:
- Detección y clasificación simultánea de múltiples objetos
- Equilibrio entre precisión y velocidad de inferencia
- Adecuado para aplicaciones industriales en tiempo real

---

## Entrenamiento
- Arquitectura: YOLOv11x  
- Entorno de entrenamiento: Google Colab  
- Hardware: GPU NVIDIA A100  
- Tiempo de entrenamiento aproximado: 8 horas  

Durante el entrenamiento se monitorizaron las métricas de pérdida y rendimiento tanto en el conjunto de entrenamiento como en el de validación, observándose una convergencia estable del modelo.

---

## Resultados
El modelo entrenado es capaz de:
- Detectar correctamente palets y paquetes en imágenes estáticas
- Realizar inferencias sobre vídeo
- Funcionar en tiempo real en escenarios logísticos

Las métricas obtenidas durante el entrenamiento y validación muestran un rendimiento sólido en términos de precisión y recall, confirmando la viabilidad del sistema para su uso en entornos reales.

---

## Uso del proyecto
El repositorio incluye:
- Código completo de entrenamiento e inferencia
- Pesos del modelo entrenado
- Ejemplos de inferencia en imágenes y vídeo

El sistema puede utilizarse para:
- Pruebas con imágenes propias
- Análisis de vídeo
- Integración en flujos de inspección automática

---

## Demo
Se ha desarrollado una página web donde se presenta el proyecto en detalle y es posible probar el modelo con imágenes o vídeos propios:

https://marcrubii.github.io/Mecalux-Pallet-Detection/

---

## Conclusiones
Este proyecto demuestra cómo las técnicas de **Deep Learning y detección de objetos** pueden aplicarse eficazmente a problemas reales de la industria logística. La combinación de un dataset propio, una arquitectura robusta y un proceso de entrenamiento controlado permite construir un sistema funcional y adaptable a distintos escenarios de inspección automática.

---

## Enlace
Página del proyecto y demo interactiva:  
https://marcrubii.github.io/Mecalux-Pallet-Detection/
