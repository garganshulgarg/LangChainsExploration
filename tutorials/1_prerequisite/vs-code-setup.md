# VS Code Setup

1. To manage Python packages within our virtual environment, we will use `pipenv` as the package manager.

2. Activating the virtual environment created by Pipenv is simple; just run the following command in the VS Code Terminal:

   ```bash
   pipenv shell

```

__Note:__ Refer to the highlighted portion in the screenshot.
![pipenv](./images/pipeenv-activate.bmp)


2. Install the `langchain` package within your virtual environment:.
```
pipenv install langchain
```
After installing `langchain``, you will find the `pipfile.lock` file in your project directory. You can search for langchain within this file.


3. Setting up the Python Interpreter in VS Code is easy. Simply press Cmd + Shift + P, and then choose the same Python interpreter as the one generated in Step 1.

4. We will be using `.env` file within this project to keep project keys

5. We have created python `launch.json` pointing to `envFile`.

6. Now, we can `RUN` & `DEBUG` the python apllication.

7. We have also installed `black` for formatting but it is totally up to you.
```
pipenv install black
```