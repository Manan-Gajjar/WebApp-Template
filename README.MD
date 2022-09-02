# Reuseable Webapp template

This template is based on open source project by [AdminLTE.io](https://adminlte.io/) that is licensed under MIT. It is created using the [flask](https://flask.palletsprojects.com/en/2.2.x/) framework in the backend and [Bootstrap](), [Jquery]() in the frontend.

## Installation

### Required Software
- [python 3.x +](https://www.python.org/)
- [Git](https://git-scm.com/download/win)
- [Visual Studio Code (vscode)](https://code.visualstudio.com/download) - optional
- [SQL Server Management Studio (SSMS)]() - optional


### Git commands

- Create folder and clone this repo  
   ```bash
    git clone https://github.com/Manan-Gajjar/WebApp-Template.git
    ```
- Create virtual environment
  ```bash
  python -m venv venv

  source venv/Scripts/activate
  ```
  
- Incase of conda environment, deactivate it - (optional if there is no conda environment)
  ```bash
  conda deactivate
  ```
  
- Install dependancy
    ```bash
    pip install -r requirement.txt
    ```
- After successful installation, run the following command.
  
  ```bash
  python run.py
  ``` 

This will spin up local flask server in you machine,
you can access app by opening [http://127.0.0.1:5000/](http://127.0.0.1:5000/) link in your browser.

## Author

* Manan Gajjar.
* Jon Peterson.


