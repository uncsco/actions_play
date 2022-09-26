## Introduction

"Building and testing Python" - **"Packaging workflow data as artifacts"**:
https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#packaging-workflow-data-as-artifacts

> "Persisting workflow data using artifacts."

https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts

> By default, GitHub **stores build logs and artifacts for 90 days**, and this retention period can be customized.

----

> - **Uploading** build and test artifacts
>
> - **Downloading** or deleting artifacts
>
> - **Passing** data between jobs in a workflow

----

### **Passing** data between jobs in a workflow

- Paste above YAML into new file: `.github/workflows/ci.yml`

- Do a 'push' - (e.g. *update* this `README.md` file)

- See 'run' details: https://github.com/uncsco/actions_play/actions/runs/3127369797/jobs/5073915890

### **Uploading** build and test artifacts

> For more information on syntax, see the `actions/upload-artifact` action.

- "Upload an Individual File": https://github.com/actions/upload-artifact#upload-an-individual-file

- See `job_0` in file `.github/workflows/ci.yml`:

```yaml

jobs:

  #// https://github.com/actions/upload-artifact#upload-an-individual-file
  job_0:
    name: Upload one file
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - run: mkdir -p test_path/artifact
    - run: echo hello > test_path/artifact/world.txt
    - uses: actions/upload-artifact@v3
      with:
        name: my-artifact
        path: test_path/artifact/world.txt
```
