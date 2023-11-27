

import streamlit as st
from PIL import Image
from segment import process

st.title('Airplane segmentation demo')

image_file = st.file_uploader('Load an image', type=['png', 'jpg'])  # ���������� ���������� ������

if not image_file is None:                       # ���������� �����, ���� ��������� �����������
    col1, col2 = st.columns(2)                   # �������� 2 ������� # st.beta_columns(2)
    image = Image.open(image_file)               # �������� �����������
    results = process(image_file)                # ��������� ����������� � ������� �������, ������������� � ������ �����
    col1.text('Source image')
    col1.image(results[0])                       # ����� � ������ ������� ������������ ��������� �����������
    col2.text('Mask')
    col2.image(results[1])                       # ����� ����� ������ �������
    st.image(results[2])                         # ����� ��������� ����������� � ���������� ������ (�� ������)
