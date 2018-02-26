import sys
import os
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(base_path)

app_path = os.path.join(base_path, 'app')
sys.path.append(app_path)