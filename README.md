# Autofill files script

Installation
------------

#### Clone a repository

```
git clone https://github.com/vadushkin/autofill-files-script.git
```

#### Change a folder

```
cd autofill-files-script
```

#### Venv

Windows:

```shell
python -m venv venv
.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

Linux:

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

#### Poetry

```
poetry install
poetry shell
```

#### Create ```.env``` file or delete ```.example``` from ```.env.example```

#### Example to fill in

```dotenv
ABSOLUTE_PATH_TO_PDFS=path/to/your/files

EMAIL=email@gmail.com
PASSWORD=password
```

```EMAIL``` and ```PASSWORD``` - credentials for the site
