

from tensorflow.keras.models import load_model
MODEL_NAME =   'model_air.h5'
import numpy as np
from PIL import Image
model = load_model(MODEL_NAME)                                              # �������� ����� ������
INPUT_SHAPE = (256, 456, 3)


def process(image_file):
    image = Image.open(image_file)  # �������� ��������������� �����
    resized_image = image.resize((INPUT_SHAPE[1], INPUT_SHAPE[0]))          # ��������� ������� ����������� � ������������ �� ������ ����
    array = np.array(resized_image)[..., :3][np.newaxis, ..., np.newaxis]   # ����������� ����� ������� ��� ������ � ����
    prediction_array = (255 * model.predict(array)).astype(int)             # ������ ������������ ����
    prediction_array = np.split(prediction_array, 2, axis = -1)[0]          # ������� ����� ������������ (�������� 0 - �������, 1 - ���)
    zeros = np.zeros_like(prediction_array)                                 # �������� ������� �����
    ones = np.ones_like(prediction_array)                                   # �������� ������� ������
    prediction_array_4d = np.concatenate([255 * (prediction_array > 100), zeros, zeros, 128 * ones], axis=3)[0].astype(np.uint8)  # ������������ ������� ��� ��������� ��������� �����
    mask_image = Image.fromarray(prediction_array_4d).resize(image.size)    # �������������� ������� � ����������� � �������� ��� ������� � ���������
    image.paste(mask_image, (0, 0), mask_image)                             # ���������� ����� �� �������� �����������
    return resized_image, prediction_array, image                           # ������� ��������� ������������ �����������, ��������� ����� � ��������� ����������� � ���������� ������
