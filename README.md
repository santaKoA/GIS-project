# GIS-project
This site is part of the GIS course project.
![logo](https://i.ibb.co/2KDC9tj/github-logo.png)

# GIS Final Project

![enter image description here](https://img.shields.io/badge/Uptime-100%25-blue) ![enter image description here](https://img.shields.io/badge/Version-Beta-green) ![enter image description here](https://img.shields.io/badge/Contributors-5-orange)


## Versions

Our site has 2 versions:

**Vulnerable version V4.2**

Vulnerable to XSS and SQLI
You can download it [HERE](https://github.com/Sagi313/computerSecurity/tree/v4.2)
This can also be found on branch `mater`

**Safe version V4.3**

Has no known vulnerabilities
You can download it [HERE](https://github.com/Sagi313/computerSecurity/tree/v4.3)
This can also be found on branch `SafeVersion`

## How to install?

1. Clone the GitHub repository to your local machine (or choose the tag you will to download)

2. Install the required dependencies. Run the following: `pip install -r requirements.txt`

3. Migrate all the DBs `python manage.py makemigrations` and then `python manage.py migrate`

4. Run the server: `python manage.py runserver` and go to http://127.0.0.1:8000/

## Touble Shooting

- If the HTTPS version doesn't load properly (Time out error), try to delete your browser cookies.


## Requirements

- Python3
- Pip3
- QGIS






