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

- Paste above YAML into new file `.github/workflows/ci.yml` - https://github.com/uncsco/actions_play/commit/6fcd83a71cf1920c5ef6c2f16db7e63b25766f56

- Do a 'push' - (e.g. *update* this `README.md` file)

- See 'run' details: https://github.com/uncsco/actions_play/actions/runs/3127369797/jobs/5073915890

### **Uploading** build and test artifacts

> For more information on syntax, see the `actions/upload-artifact` action.

- "Upload an Individual File": https://github.com/actions/upload-artifact#upload-an-individual-file

- See `job_0` in file `.github/workflows/ci.yml`: https://github.com/uncsco/actions_play/commit/5ccb14dc0c0d0198453102d8cce8f5f5b004c495

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

### **Downloading** or deleting artifacts

> **Note:** You can only download artifacts in a workflow that were uploaded during the same workflow run.

// `WIP`...

- See: https://github.com/uncsco/actions_play/commit/0a004cf6826fb9c894820b1bc7072c149207fe81
