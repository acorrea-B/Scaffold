
## Badges

[![Python application test with Github Actions](https://github.com/acorrea-B/Scaffold/actions/workflows/main.yml/badge.svg)](https://github.com/acorrea-B/Scaffold/actions/workflows/main.yml)
# Scaffold
On this repository, we gonna test GitHub Actions with python code

## Demo

Insert gif or link to demo


## Main code

```bash
name: Python application test with Github Actions

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v1
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        make install
    - name: Lint with pylint
      run: |
        make lint
    - name: Test with pytest
      run: |
        make test
    - name: Format code
      run: |
        make format
    
    
```

