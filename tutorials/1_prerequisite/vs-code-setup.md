# VS Code Setup

1. To manage Python packages within our virtual environment, we will use `poetry` as the package manager.

2. Activating the virtual environment created by Poetry is simple; just run the following command in the VS Code Terminal:

```bash
   poetry init
   poetry config virtualenvs.in-project true
   poetry install
   poetry shell

```



2. Install the `langchain` & `openai` package within your virtual environment:.
```bash
poetry add langchain
poetry add openai

```

After installing `langchain` & `openai`, you will find the `poetry.lock` file in your project directory. You can search for langchain within this file.


3. Setting up the Python Interpreter in VS Code is easy. Simply press Cmd + Shift + P, and then choose the same Python interpreter as the one generated in Step 1.

4. We will be using `.env` file within this project to keep project keys

5. We have created python `launch.json` pointing to `envFile`.

6. Now, we can `RUN` & `DEBUG` the python apllication.

7. We have also installed `black` for formatting but it is totally up to you.

```bash
poetry add black
```


8. For exiting out of `poetry` type in `exit`
9. For activating venv use `activate` and for deactivating use `deactivate`




## Troubleshooting

`pyenv` is a prerequisite for poetry.

You might need to execute following commands

```bash
pyenv init
```

Update your `~/.zshrc` with output recieved from above command

Execute following more commands

```bash
pyenv install --list
pyenv install 3.9.18
pyenv local 3.9.18
```
