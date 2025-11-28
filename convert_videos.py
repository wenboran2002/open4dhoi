import os
import subprocess
from pathlib import Path

def convert_video(input_path):
    """Convert video to H.264 mp4 for web compatibility."""
    output_path = str(input_path).replace('.mp4', '_web.mp4')
    
    # ffmpeg command: 
    # -c:v libx264: use H.264 codec
    # -pix_fmt yuv420p: ensure compatibility with all players
    # -movflags +faststart: optimize for web streaming
    # -y: overwrite output
    cmd = [
        'ffmpeg', '-i', str(input_path),
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-movflags', '+faststart',
        '-y',
        output_path
    ]
    
    print(f"Converting {input_path} -> {output_path}...")
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Replace original with new file
        os.replace(output_path, input_path)
        print(f"Success: {input_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_path}: {e}")

def main():
    # Target directory
    video_dir = Path('/data/boran/4dhoi/PROJECTS/open4dhoi/static/images')
    
    # Find all _org.mp4 files
    videos = list(video_dir.glob('*_org.mp4'))
    
    if not videos:
        print("No *_org.mp4 files found.")
        return

    for vid in videos:
        convert_video(vid)

if __name__ == '__main__':
    main()
