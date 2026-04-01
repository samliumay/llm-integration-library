# Python Virtual Environment on Windows

A quick guide to creating and using a Python virtual environment on Windows.

## Create a Virtual Environment

```
python -m venv closed-model-api-managment
```

## Activate

**Command Prompt:**
```
closed-model-api-managment\Scripts\activate
```

**PowerShell:**
```
closed-model-api-managment\Scripts\Activate.ps1
```

You'll see `(closed-model-api-managment)` in your terminal when it's active.

## Install Packages

```
pip install package_name
```

## Deactivate

```
deactivate
```

## Troubleshooting

If PowerShell gives an execution policy error, run:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```