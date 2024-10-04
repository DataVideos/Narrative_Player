import os
import subprocess

# 获取当前目录下所有 mp4 文件
video_files = [f for f in os.listdir() if f.endswith('.mp4')]

for video in video_files:
    # 获取文件名（不带扩展名）
    filename = os.path.splitext(video)[0]

    # 定义输出图片的名称
    output_image = f"{filename}_last_frame.png"

    # 提取最后一帧
    command = ['ffmpeg', '-sseof', '-0.5', '-i', video, '-vframes', '1', output_image]

    # 执行命令
    subprocess.run(command)

    print(f"提取了 {video} 的最后一帧，保存为 {output_image}")

