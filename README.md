# Scolagile tracker
This script will show a notification in your computer if a professor changed any of your scolagile notes while it's running.
To use it, you first will have to create a `.env` file following this format
```env
USERNAME=yourusername
PASSWORD=yourpassword
```
then you'll have to install the python dependencies
```bash
pip install -r requirements.txt
```
then install playwrite's browser
```bash
playwrite install
```

# Compiling
to compile this project you can user [pyinstaller](https://pyinstaller.org/en/stable/)
```bash
pyinstaller -i icon/exe.ico -F -w gui.py
```