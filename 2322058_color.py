import numpy as np
import matplotlib.pyplot as plt

# 画像の正規化されたピクセル値が入った配列
normalized_image = np.random.rand(100, 100)  # 仮の正規化された画像

# 元のピクセル値の範囲を指定
original_min = 0
original_max = 255  # 例として、8ビットのグレースケール画像の場合

# 正規化を元に戻す
restored_image = (normalized_image * (original_max - original_min)) + original_min

# 画像を表示
plt.imshow(restored_image, cmap='gray')  # グレースケール画像の場合
plt.axis('off')
plt.show()
