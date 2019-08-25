# LMAKE

Live Reloading facility for all programming languages.

# Install Instructions

Download the repo as a zip and extract it.
Then run:
``` sh install.sh ```
It will ask for root privilege. If not given, every time the terminal is loaded, you have to run
``` source ~/.profile ```

# Usage

Instead of compiling normally, do:
``` lmake <file.extension> ```
It will take appropriate compilation steps as per the programming language.
File will be compiled and will start running. Now each time you make any change to the source file, lmake will automatically detect the change and recompile your program and rerun.

If you want separate compiling and running instructions to be executed, consider creating a config file in your program directory and run:
``` lmake <file.extension> -c <conf.json> ```
The details of the config file is described later.

If you want to specify a separate input file, you can run with `-i <input_file_name>` flag.

# Contributing

Raise issues and send PRs if you want to make the code better.
But more importantly, we need configs for various programming languages.
To create a config, create a ` <target_file_extension>.json` file in the config directory.
Then insert the following in it:

```json
    {
    "compile": "<Most common compile instruction>",
    "run": "<Most common running instruction>"
    }

```
You can use 2 variables, `?fpath?` and `?name?` for source code path (with extension) and source code name (without extension) respectively.
``` 