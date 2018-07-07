# -*- coding: UTF-8 -*-

import unittest
from main import get_target_file_list


# get_target_file_listのテスト
class TestGetTargetFileList(unittest.TestCase):

    # 正常パターン
    # 対象ディレクトリ、対象ファイルが存在する場合
    def test_target_file_exists(self):
        # 対象のファイルのあるディレクトリ
        target_dir = '../target'

        # 顔画像生成先
        output_dir = '../output'

        # 想定値
        expected = ['/home/kento/PycharmProjects/face-trim/target/2999_p0.png',
                    '/home/kento/PycharmProjects/face-trim/target/5724612_p0.jpg',
                    '/home/kento/PycharmProjects/face-trim/target/27218456_p0.jpg',
                    '/home/kento/PycharmProjects/face-trim/target/20703886_p0.jpg',
                    '/home/kento/PycharmProjects/face-trim/target/1552792_p0.jpg',
                    '/home/kento/PycharmProjects/face-trim/target/30973729_p0.jpg',
                    '/home/kento/PycharmProjects/face-trim/target/42960677_p0.jpg',
                    '/home/kento/PycharmProjects/face-trim/target/365278_p0.png']

        # テストモジュール実行
        result = get_target_file_list(target_dir)

        # 想定値との比較
        self.assertEqual(result, expected, 'Match expected value')


if __name__ == '__main__':
    unittest.main()
