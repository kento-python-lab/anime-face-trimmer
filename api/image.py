#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import cv2
from PIL import Image
from .util import get_suffix


class InvalidImageFormatError(BaseException):
    pass


def get_faces(img_path, cascade_file):
    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(24, 24))
    return faces


def crop_face(image_path, face, min_size=(120, 120)):
    if not get_suffix(image_path):
        raise InvalidImageFormatError('拡張子エラー')

    img = Image.open(image_path)
    x1, y1, x2, y2 = (face[0], face[1], face[0] + face[2], face[1] + face[3])
    cropped = img.crop((x1, y1, x2, y2))

    if cropped.size[0] <= min_size[0] or cropped.size[1] <= min_size[1]:
        raise InvalidImageFormatError('サイズが規定値以下')

    return cropped
