import subprocess

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(script_dir, 'src'))

subprocess.Popen(['streamlit', 'run', 'Home.py'])