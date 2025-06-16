# Build

I used [_**cx_Freeze**_](https://github.com/marcelotduarte/cx_Freeze) to "package" the project, and it's working perfectly. However, you’re obviously free to choose/test another packager if you prefer.

> [!NOTE]
> Since I wanted to leave the choice of packager open, I decided not to include the setup.py file for cx_Freeze in the repository. Still, I’ll leave the code I used for the build below.

```py
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

### Build Command:

```
python setup.py build
```

###

# About

This is a personal app designed to create a sleep timer for PC (Windows and Linux). I often needed to leave my computer on while I was asleep or away, but I didn’t want it running unnecessarily.

For years, I used a collection of _**.bat**_ files, each one containing commands to shut the PC down after a set amount of time.

Since I’ve been learning to program for a few years now, I decided to update this "system" (if I can call it that).

Of course, I could have just searched for and downloaded a program that does this. But apart from being cautious about the kinds of software I install on my PC, I also saw this as a good learning opportunity — especially because up to now, I’ve focused more on web technologies.

That’s it! There’s still a lot I’d like to improve and add over time, as time and resources allow. But for now, all the available features are working perfectly.
