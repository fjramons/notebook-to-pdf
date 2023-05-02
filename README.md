# Notebook-to-PDF: Helper for optimized conversion of Jupyter Notebooks to PDF

Helper tool to automate production of PDF documents from Jupyter Notebooks (`.ipynb`) with the appropriate metadata, such as:

- Title.
- Authors.
- Date (if not today's date)
- etc.

## Usage

It can run from as a Python script or as a container (recommended).

### From container

```bash
docker run -it --rm fjramons/notebook2pdf \
    source_notebook.ipynb metadata.yaml destination_notebook.ipynb
```

Where:

- `source_notebook.ipynb`: Original notebook, without metadata.
- `metadata.yaml`: YAML file with medatada. An example can be found at `examples/metadata.yaml`.
- `destination_notebook.ipynb` (optional): Destination name for the notebook where metadata is inserted. In case it is omitted, the original notebook is overwritten.

#### Use after installation (recommended)

For simpler use, a convenience alias can be installed at `.bashrc` by:

```bash
./scripts/install-nb2pdf.sh
```

This alias will allow running the container as if it where a regular command line tool:

```bash
nb2pdf source_notebook.ipynb metadata.yaml destination_notebook.ipynb
```

**NOTE:** The alias mounts the current dir (regardless the current location) as the container's workdir and exits whenever finishes.

Alternatively, for a temporary use, you can also load the alias by running `source ./scripts/source-alias.sh`

### As Python script

#### Pre-requirements

- `pandoc`
- `texlive-fonts-recommended`
- `texlive-plain-generic`
- `texlive-xetex`
- Python packages:
  - The ones specified at `requirements.txt` (same packages for `pip` and `conda`).

#### Script usage

```bash
python3 ./src/add-metadata.py \
    source_notebook.ipynb metadata.yaml destination_notebook.ipynb
```
