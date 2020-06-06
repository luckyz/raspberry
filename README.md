## Packages and configurations

To configurate and install necesary packages, first, get superuser privileges with `sudo -s` command. Then, run `setup.py` typing in a terminal:

```
python setup.py
```

or:

```
./setup.py
```

Note: you can run this command periodically.

## Raspberry GPIO templates

To generate predefined python files to control GPIO pins, run this in a terminal, outside `templates/` dir:

```
cp templates/base.py new_name_of_file.py
```

or:

```
python templates/bash_profile.py
```
