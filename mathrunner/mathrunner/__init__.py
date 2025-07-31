#------------------------------------------------------------------------------#

import subprocess
from pathlib import Path

print('__init__')

here = Path(__file__).parent

subprocess.run([
    'pyside6-rcc', 
    here/'resources.qrc',
    '-o', here/'resources_rc.py'
])

for ui_file in here.glob('*.ui'):
    py_file = ui_file.with_suffix('.py')
    subprocess.run([
        'pyside6-uic', 
        '-g', 'python', ui_file, 
        '-o', py_file
    ])

#------------------------------------------------------------------------------#