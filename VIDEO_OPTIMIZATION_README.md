# Video Optimization for Fast Seeking

## Problem
Video progress bar dragging was very laggy due to poor seeking performance in WebM videos.

## Solution
Re-encoded all WebM videos with optimized VP9 encoding parameters for fast seeking:

### Key Changes
1. **Keyframe Interval**: Set to 30 frames (1 second at 30fps) with `-g 30`
2. **Minimum Keyframe Distance**: Set to 30 frames with `-keyint_min 30`
3. **Bitrate**: Reduced to 800K for better performance
4. **Codec Settings**: Added VP9-specific optimizations (`-deadline good`, `-cpu-used 2`)
5. **HTML Attributes**: Added `preload="metadata"` to all video elements

### Technical Details
- **Before**: Videos encoded with default VP9 settings, causing slow seeking
- **After**: Videos optimized with frequent keyframes for instant seeking
- **Format**: VP9/WebM maintained for web compatibility
- **File Size**: Slightly smaller due to optimized bitrate

### Files Modified
- `convert_videos_optimized.py`: Updated conversion script with seeking optimizations
- `index.html`: Added `preload="metadata"` to all video elements
- All `.webm` files in `static/images/` and `static/images/physics/`: Re-encoded

### Usage
Run `python convert_videos_optimized.py` to re-encode any new videos added to the project.

## Result
Video progress bar dragging is now smooth and responsive across all browsers.