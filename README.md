# Commandline interface utility for MongoDB
Simple and useful utility for:

- uploading

- downloading

- listing 

- deleting

files from/to MongoDB

## Project structure
``` bash
├── README.md
├── .gitignore
├── dal
│   ├── client.py
│   ├── operations.py
├── fs_utility
│   ├── reader.py
│   └── writer.py
├── delete.py
├── download.py
├── upload.py
├── list.py
├── requirements.txt
├── .env_example
```

### Setup the project for the development

pip install -r requirements-dev.txt

### Run
```bash
python list.py
python delete.py -id <id>
python download.py -o <path/file> -id <id>
python  upload.py --input <path/file>
```


### Linting
```bash
flake8 
```