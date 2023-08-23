from gtts import gTTS
import subprocess

def split_text_into_lines(text, max_line_length):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += " " + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return '\n'.join(lines)

def create_image_with_text(image_path, output_image_path, formatted_text, font_path, font_size, text_color, x_position, y_position):
    ffmpeg_command = [
        pathFFmpeg,
        '-i', image_path,
        '-vf', f"drawtext=text='{formatted_text}':fontfile={font_path}:fontcolor={text_color}:fontsize={font_size}:x={x_position}:y={y_position}",
        output_image_path
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print("Image with left-aligned and centered text creation successful.")
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e)

def convert_text_to_speech(text, output_audio_path):
    tts = gTTS(text, lang='en')
    tts.save(output_audio_path)
    print("Text to speech conversion successful.")

def create_video_with_overlay(video_path, image_path, output_audio_path, output_video_path, overlay_duration, zoom_duration):
    ffmpeg_command = [
        pathFFmpeg,
        '-i', video_path,
        '-loop', '1',
        '-t', str(100),
        '-i', image_path,
        '-i', output_audio_path,
        '-filter_complex',
        f"[0:v][1:v]overlay=(W-w)/2:(H-h)/2:enable='between(t,0,{overlay_duration})',zoompan=z='if(lte(pzoom,1.0),max(1.001,pzoom-{3/zoom_duration}),1.09)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={zoom_duration}[v1];" +
        f"[2:a][0:a]amerge=inputs=2[a];" +
        f"[2:a]showwaves=s=120x120:colors=black:mode=cline[waveform];" +
        "[v1][waveform]overlay=x=((W-w)/2)+150:y=(H-h)/2-50:shortest=1[v]",
        '-map', '[v]',
        '-map', '[a]',
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-pix_fmt', 'yuv420p',
        output_video_path
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print("Video with overlay creation successful.")
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    pathFFmpeg = r'E:\courses\ffmpeg-5.1.2-full_build\ffmpeg-5.1.2-full_build\bin\ffmpeg.exe'
    image_path = 'resizedImage.png'
    output_image_path = 'output_image_left_aligned.png'
    text = "Hello. This is the sample input."
    font_path = "calibri-bold.ttf"
    font_size = 20
    text_color = 'black'
    x_position = 10
    y_position = '(h-text_h)/2+2'
    max_line_length = 30

    formatted_text = split_text_into_lines(text, max_line_length)
    create_image_with_text(image_path, output_image_path, formatted_text, font_path, font_size, text_color, x_position, y_position)
    convert_text_to_speech(text, 'output_audio.mp3')

    video_path = 'videos\y2.mp4'
    output_video_path = 'output_video_with_overlay.mp4'
    overlay_duration = 2
    zoom_duration = 2

    create_video_with_overlay(video_path, output_image_path, 'output_audio.mp3', output_video_path, overlay_duration, zoom_duration)
