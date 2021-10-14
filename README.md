# Python Basics

### Create a virtual environment
```bash
# Note that python could be installed as python3
python -m venv my-virtual-env
```

### Activate / load a virtual environment
```bash
# On Linux
source my-virtual-env/bin/activate

# On Windows
my-virtual-env\Scripts\activate.bat
```

### Install a new dependency / library
```bash
python -m pip install <library-name>

# Example
python -m pip install numpy
```

### Generate requirements.txt file for registering dependencies
```bash
python -m pip freeze > requirements.txt
```

### Install dependencies from requirements.txt
```bash
python -m pip install -r requirements.txt
```

## References
[Reference](https://towardsdatascience.com/virtual-environments-104c62d48c54)