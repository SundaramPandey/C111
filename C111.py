import os
import shutil

from_dir="C:/Users/slane/Downloads/C102_assets-main/C102_assets-main"
to_dir="C:/Users/slane/OneDrive/Documents/whjr python"
all_files=os.listdir(from_dir)
print(all_files)
for i in all_files:
    print(os.path.splitext(i))