# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Main_UI.py'],
    pathex=[],
    binaries=[],
    datas=[('Glitch_number.gif', '.'), ('Areaofcircle.png', '.'), ('Rectangle_area.png', '.'), ('Right_triangle.png', '.'), ('Triangle_areaimg.png', '.'), ('Regular_polygon.png', '.'), ('Quadratic_formula_img.png', '.'), ('Factorial.png', '.'), ('Algebra_expression.png', '.'), ('Calc_icon.ico', '.'), ('PressStart2P-Regular.ttf', '.'), ('C:\\Users\\nisha\\AppData\\Local\\Python\\pythoncore-3.12-64\\Lib\\site-packages\\customtkinter', 'customtkinter')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Main_UI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Calc_icon.ico'],
)
