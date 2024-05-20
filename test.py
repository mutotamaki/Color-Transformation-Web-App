from PIL import Image
import numpy as np
import gradio as gr

def image_to_normalized_vector(image):
    
    # 画像をRGB形式に変換（必要であれば）
    img = image.convert('RGB')
    
    # 画像データをNumPy配列に変換
    img_array = np.array(img)
    
    # RGB値を0-1の範囲に正規化
    normalized_array = img_array / 255.0
    
    return normalized_array, img.size

def normalized_vector_to_image(normalized_array, size):
    # 正規化された配列を元のスケールに戻す
    img_array = (normalized_array * 255).astype(np.uint8)
    
    # 配列を画像に変換
    img = Image.fromarray(img_array, 'RGB')
    
    # 元の画像のサイズにリサイズ
    img = img.resize(size)
    
    return img

def apply_color_transform(normalized_array, transform_matrix):
    # 画像の形状を取得
    original_shape = normalized_array.shape
    
    # 1次元ベクトルに変換
    flat_array = normalized_array.reshape(-1, 3)
    
    # 線形変換を適用
    transformed_flat_array = flat_array @ transform_matrix.T
    
    # 変換後の値が0-1の範囲に収まるようにクリッピング
    transformed_flat_array = np.clip(transformed_flat_array, 0, 1)
    
    # 元の形状に戻す
    transformed_array = transformed_flat_array.reshape(original_shape)
    
    return transformed_array

# 変換行列（3×3のランダム行列を生成）
transform_matrix = np.random.rand(3, 3)

def process_image(image):
    normalized_array, size = image_to_normalized_vector(image)
    transformed_array = apply_color_transform(normalized_array, transform_matrix)
    transformed_image = normalized_vector_to_image(transformed_array, size)
    return transformed_image

iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil"),
    outputs="image"
)

iface.launch()
