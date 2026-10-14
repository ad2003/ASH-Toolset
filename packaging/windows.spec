from pathlib import Path
from PyInstaller.utils.hooks import collect_all

root = Path(SPECPATH).parent
datas = [(str(root / 'data'), 'data'),
         (str(root / 'metadata.json'), '.'),
         (str(root / 'LICENSE'), '.')]
binaries = []
hiddenimports = []
# Include dynamically imported modules and package resources used in DSP/UI.
for package in ('librosa', 'sofar', 'SOFASonix', 'dearpygui_ext',
                'dearpygui_extend', 'noisereduce', 'mat73'):
    package_datas, package_binaries, package_imports = collect_all(package)
    datas += package_datas
    binaries += package_binaries
    hiddenimports += package_imports

a = Analysis([str(root / 'packaging' / 'entrypoint.py')],
             pathex=[str(root)], binaries=binaries, datas=datas,
             hiddenimports=hiddenimports)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True,
          name='ASH-Toolset', console=False,
          icon=str(root / 'data' / 'raw' / 'ash_icon_1.ico'))
coll = COLLECT(exe, a.binaries, a.datas, name='ASH-Toolset')
