#------------------------------------------------------------------------------#

import subprocess
from pathlib import Path

here = Path(__file__).parent

rc_qt = here / 'resources.qrc'
rc_py = here / 'resources_rc.py'

if not rc_py.exists() or rc_py.stat().st_mtime < rc_qt.stat().st_mtime:
    subprocess.run(['pyside6-rcc', rc_qt, '-o', rc_py])

for ui_file in here.glob('*.ui'):
    py_file = ui_file.with_suffix('.py')

    if not py_file.exists() or py_file.stat().st_mtime < ui_file.stat().st_mtime:
        subprocess.run(['pyside6-uic', '-g', 'python', ui_file, '-o', py_file])

file = here / 'form_main_window.py'

content = file.read_text()
content = content.replace('import resources_rc', 'from . import resources_rc')

file.write_text(content)

#------------------------------------------------------------------------------#