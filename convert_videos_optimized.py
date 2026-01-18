import os
import subprocess
from pathlib import Path

def convert_to_webm(input_path):
    """Convert video to VP9/Opus WebM optimized for fast seeking."""
    output_path = str(input_path).replace('.mp4', '.webm')

    # ffmpeg command optimized for web video seeking:
    # -c:v libvpx-vp9: use VP9 codec (modern, efficient, web-friendly)
    # -b:v 800K: lower bitrate for better performance
    # -g 30: keyframe every 30 frames (1 second at 30fps) for fast seeking
    # -keyint_min 30: minimum keyframe interval
    # -c:a libopus: use Opus audio codec
    # -deadline good: balance quality/speed (good is default)
    # -cpu-used 2: CPU usage optimization
    # -y: overwrite output
    cmd = [
        'ffmpeg', '-i', str(input_path),
        '-c:v', 'libvpx-vp9',
        '-b:v', '800K',
        '-g', '30',
        '-keyint_min', '30',
        '-c:a', 'libopus',
        '-deadline', 'good',
        '-cpu-used', '2',
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
    # Target directories
    video_dirs = [
        Path('/data/boran/4dhoi/PROJECTS/open4dhoi/static/images'),
        Path('/data/boran/4dhoi/PROJECTS/open4dhoi/static/images/physics')
    ]

    all_videos = []
    for video_dir in video_dirs:
        # Find all .mp4 files (we'll overwrite existing .webm files with optimized versions)
        videos = list(video_dir.glob('*.mp4'))
        all_videos.extend(videos)

    if not all_videos:
        print("No .mp4 files found that need conversion.")
        return

    print(f"Found {len(all_videos)} videos to convert...")
    for vid in all_videos:
        convert_to_webm(vid)

if __name__ == '__main__':
    main()
