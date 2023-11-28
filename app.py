import os
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

# Остальной код вашего приложения...

import streamlit as st
from PIL import Image
from segment import process

st.title('Different images segmentation demo')

image_file = st.file_uploader('Load an image', type=['png', 'jpg'])  # Добавление загрузчика файлов

if image_file is not None:  # Выполнение блока, если загружено изображение
    try:
        # Попытка открыть изображение
        image = Image.open(image_file)

        # Ваш код для обработки изображения
        col1, col2 = st.columns(2)
        results = process(image_file)
        col1.text('Source image')
        col1.image(results[0])
        col2.text('Mask')
        col2.image(results[1])
        st.image(results[2])

    except UnicodeDecodeError as e:
        # Обработка ошибки декодирования
        st.error(f"Ошибка декодирования файла: {e}")
