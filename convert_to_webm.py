import os
import subprocess
from pathlib import Path

def convert_to_webm(input_path):
    """Convert video to VP9/Opus WebM for maximum web compatibility."""
    output_path = str(input_path).replace('.mp4', '.webm')
    
    # ffmpeg command: 
    # -c:v libvpx-vp9: use VP9 codec (modern, efficient, web-friendly)
    # -b:v 1M: target bitrate (adjust as needed)
    # -c:a libopus: use Opus audio codec
    # -y: overwrite output
    cmd = [
        'ffmpeg', '-i', str(input_path),
        '-c:v', 'libvpx-vp9',
        '-b:v', '1M',
        '-c:a', 'libopus',
        '-y',
        output_path
    ]
    
    print(f"Converting {input_path} -> {output_path}...")
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Success: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_path}: {e}")
        return None

def main():
    # Target directory
    video_dir = Path('/data/boran/4dhoi/PROJECTS/open4dhoi/static/images')
    
    # Find all _org.mp4 files
    videos = list(video_dir.glob('*_org.mp4'))
    
    if not videos:
        print("No *_org.mp4 files found.")
        return

    for vid in videos:
        convert_to_webm(vid)

if __name__ == '__main__':
    main()
