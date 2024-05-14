# 表現行列を作る
import numpy as np

# 3×3のランダム行列を生成
transform_matrix = np.random.rand(3, 3)

y_bector = np.dot(transform_matrix, normalized_vector)
#正規化したRGBベクトル