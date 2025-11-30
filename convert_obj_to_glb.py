import trimesh
import os
from pathlib import Path

source_dir = Path('/data/boran/4dhoi/PROJECTS/open4dhoi/static/3d_models')
files = list(source_dir.glob('*.obj'))

for file_path in files:
    print(f"Processing {file_path}...")
    try:
        # force='mesh' to ensure we get a mesh if possible, but obj often loads as Scene if multiple objects
        # actually load() is smart enough.
        mesh = trimesh.load(file_path)
        
        output_path = file_path.with_suffix('.glb')
        mesh.export(output_path)
        print(f"Exported to {output_path}")
    except Exception as e:
        print(f"Failed to convert {file_path}: {e}")
