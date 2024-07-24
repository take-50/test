# pip install streamlit
# pip install streamlit-cropper
# pip install numpy  
# pip install pandas
# pip install Pillow

# 必要なライブラリをインポート
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_cropper import st_cropper
from PIL import Image

# タイトルとテキストを記入
st.title('Streamlit 基礎')
st.write('Hello World!')


# セレクトボックス
option = st.sidebar.selectbox(
    '好きな数字を入力してください。',
    list(range(1, 11))
)
'あなたの好きな数字は' , option , 'です。'

# スライダーによる値の動的変更
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：' , condition

# テキスト入力による値の動的変更
text = st.sidebar.text_input('あなたの好きなスポーツを教えて下さい。')
'あなたの好きなスポーツ：' , text

# 画像アップロード＆枠の比率
st.set_option('deprecation.showfileUploaderEncoding', False)
# Upload an image and set some options for demo purposes
st.header("Cropper Demo")
img_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg'])
realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
# aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["Free"])
aspect_dict = {
    "Free": None,
    "1:1": (1, 1),
    "16:9": (16, 9),
    "4:3": (4, 3),
    "2:3": (2, 3),
}
aspect_ratio = aspect_dict[aspect_choice]
# サイドバーで回転角度を指定
angle_choice = st.sidebar.radio(label="Aspect Ratio", options=["0", "90", "180", "270"])
angle_dict = {
    "0": (0),
    "90": (90),
    "180": (180),
    "270": (270),
}
rotation_angle = angle_dict[angle_choice]

if img_file:
    img = Image.open(img_file)
    if not realtime_update:
        st.write("Double click to save crop")
    # Get a cropped image from the frontend
    cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                                aspect_ratio=aspect_ratio)
    
     # クロップされた画像を表示
    st.write("Preview")
    _ = cropped_img.thumbnail((150, 150))
    
    # クロップされた画像を回転
    rotated_img = cropped_img.rotate(rotation_angle, expand=True)
    
    # 回転後の画像を表示
    st.image(rotated_img, caption=f'Rotated Image by {rotation_angle} degrees', use_column_width=True)
       
# チェックボックス
if st.checkbox('Show Image'):
    # 回転後の画像を表示
    st.image(rotated_img, caption=f'Rotated Image by {rotation_angle} degrees', use_column_width=True)
    
# 画像のサイズ取得
w, h = img.size
# 拡張されたキャンバスサイズを計算
new_w = int((w**2 + h**2)**0.5)
new_h = new_w
# 拡張されたキャンバスの作成と元の画像の配置
expanded_img = Image.new("RGBA", (new_w, new_h), (255, 255, 255, 0))
expanded_img.paste(img, ((new_w - w) // 2, (new_h - h) // 2))
# 画像を回転させる（例えば、90度回転）
rotated_img = expanded_img.rotate(270, expand=True)
# 回転した画像を表示
st.image(rotated_img, caption='Rotated Iris', use_column_width=True)

# プロットする乱数をデータフレームで用意
# 宝塚市の緯度と経度
takarazuka_lat = 34.8
takarazuka_lon = 135.3

# 宝塚市の緯度と経度の範囲
lat_range = [34.74, 34.86]
lon_range = [135.24, 135.36]

# 乱数を生成し、宝塚市内に収める
df = pd.DataFrame(
    # np.random.rand(100, 2) * [lat_range[1] - lat_range[0], lon_range[1] - lon_range[0]] + [lat_range[0], lon_range[0]],
    np.random.rand(100, 2) * [lat_range[1] - lat_range[0], lon_range[1] - lon_range[0]] + [lat_range[0], lon_range[0]],
    columns=['lat', 'lon']
)

# マップをプロット
st.map(df)

# データフレームの準備
df = pd.DataFrame({
    '1列目' : [1, 2, 3, 4],
    '2列目' : [10, 20, 30, 40]
})

# 動的なテーブル
st.dataframe(df)

# 引数を使用した動的テーブル
st.dataframe(df.style.highlight_max(axis = 0) , width = 100 , height = 150)

# 静的なテーブル
st.table(df)

# 10 行 3 列のデータフレームを準備
df = pd.DataFrame(
    np.random.rand(10,3),
    columns = ['a', 'b', 'c']
)
df

# 折れ線グラフ
st.line_chart(df)

# 面グラフ
st.area_chart(df)

# 棒グラフ
st.bar_chart(df)