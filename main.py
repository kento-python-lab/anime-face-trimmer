import os
import sys
import glob

from api.image import InvalidImageFormatError, get_faces, crop_face
from api.util import get_suffix


def main():
    # 対象のファイルのあるディレクトリ
    target_dir = './target'

    # 顔画像生成先
    output_dir = './output'

    # 対象となるファイルの取得
    file_list = get_target_file_list(target_dir)

    # 対象ファイルから顔画像のみの画像を生成
    face_image_create(file_list, output_dir)


# 対象ファイルのリストを生成
def get_target_file_list(target_dir):
    image_list = list(os.path.abspath(p) for p in glob.glob(target_dir + '/*'))

    return image_list


# 対象ファイルのリストから顔画像を生成
def face_image_create(file_list, output_dir):

    # ファイル
    for count, file_name in enumerate(file_list):
        # faceディレクトリ作成
        if not os.path.exists(f'{output_dir}'):
            os.mkdir(f'{output_dir}')

            try:
                faces = get_faces(file_name)
            except Exception as e:
                print(e, file=sys.stderr)
                continue

            for face in faces:
                suffix = get_suffix(file_name)
                try:
                    img = crop_face(file_name, face)
                except InvalidImageFormatError:
                    continue
                except Exception as e:
                    print(e, file=sys.stderr)
                    continue
                face_filename = f'{output_dir}/{str(count).zfill(3)}{suffix}'
                img.save(face_filename)
                count += 1


if __name__ == '__main__':
    main()
