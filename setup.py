from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pynput", "pil"]}
target = Executable(
    script="app.py",
    icon="among_us_bot.ico"
)

setup(
    name="Among Us Bot",
    version="0.1",
    description="Solves the wiring task in Among Us",
    author="Christophe RUIZ",
    options={"build_exe": build_exe_options},
    executables=[target],
)
