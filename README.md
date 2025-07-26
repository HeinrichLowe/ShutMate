# Build

I tested [_**PyInstaller**_](https://github.com/pyinstaller/pyinstaller) and [_**cx_Freeze**_](https://github.com/marcelotduarte/cx_Freeze) to package the project, and both work perfectly. However, you’re obviously free to choose or test another packager if you prefer.

> [!NOTE]
> Since I wanted to leave the choice of packager open, I decided not to include the setup file for [_**PyInstaller**_](https://github.com/pyinstaller/pyinstaller) or [_**cx_Freeze**_](https://github.com/marcelotduarte/cx_Freeze) in the repository. Still, I’ll leave the code I used for the build below.

### 1. It is highly recommended to use a virtual environment to install all necessary dependencies.

```
python -m venv venv
```

### 2. Make sure the virtual environment is activated. If not, activate it.

_**Windows**_

```
venv/scripts/activate
```

_**Linux**_

```
source venv/bin/activate
```

### 3. Now you need to install all the dependencies.

```
pip install -r requirements.txt
```

### 4. Next, choose which packager you will use and follow its step-by-step instructions.

#### PyInstaller _(recommended)_

_**Installing**_

```
pip install pyinstaller
```

_**Building**_

_**Windows**_

```bat
pyinstaller main.py ^
    --name "ShutMate" ^
    --add-data "app/assets/images;app/assets/images" ^
    --add-data "app/assets/css;app/assets/css" ^
    --icon="app/assets/images/shutmate.ico" ^
    --noconsole ^
    --onefile
```

_**Linux**_

```sh
pyinstaller main.py \
    --name "ShutMate" \
    --add-data "app/assets/images:app/assets/images" \
    --add-data "app/assets/css:app/assets/css" \
    --icon="app/assets/images/shutmate.ico" \
    --noconsole \
    --onefile
```

##### PyInstaller Build Command:

_**Windows**_

```
.\setup.bat
```

_**Linux**_

```
./setup.sh
```

> [!NOTE]
> The PyInstaller build command above is only necessary if you decide to create a **`.bat`** or **`.sh`** file _(which I highly recommend for testing and easier visualization)_. You can simply copy the command below into the terminal if you prefer.

```
pyinstaller main.py --name "ShutMate" --add-data "app/assets/images;app/assets/images" --add-data "app/assets/css;app/assets/css" --icon="app/assets/images/shutmate.ico" --noconsole --onefile
```

#### cx_Freeze

_**Installing**_

```
pip install cx-Freeze
```

_**Building**_

```python
import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", "PyQt6"],
    "include_files": [
        ("app/assets/images", "app/assets/images"),
        ("app/ui/main_window/style.css", "app/ui/main_window/style.css"),
    ],
}

setup(
    name="ShutMate",
    version="1.0",
    description="Sleep timer for PC (Windows and Linux).",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "main.py",
            base="Win32GUI" if sys.platform == "win32" else None,
            target_name="ShutMate.exe",
            icon="app/assets/images/shutmate.ico",
        )
    ],
)
```

##### cx_Freeze Build Command:

```
python setup.py build
```

###

# About

This is a personal app designed to create a sleep timer for PC (Windows and Linux). I often needed to leave my computer on while I was asleep or away, but I didn’t want it running unnecessarily.

For years, I used a collection of _**`.bat`**_ files, each containing commands to shut the PC down after a set amount of time.

Since I’ve been learning to program for a few years now, I decided to update this "system" (if I can call it that).

Of course, I could have just searched for and downloaded a program that does this. But apart from being cautious about the kinds of software I install on my PC, I also saw this as a good learning opportunity — especially because up to now, I’ve focused more on web technologies.

That’s it! There’s still a lot I’d like to improve and add over time, as time and resources allow. But for now, all the available features are working perfectly.
