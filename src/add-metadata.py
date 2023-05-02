#!/usr/bin/python3

# %%
import json
import yaml
import click
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import PDFExporter
from pathlib import Path


def add_metadata(in_notebook_file, out_notebook_file, in_metadata_file):
    """Adds metadata to .ipynb notebook

    Args:
        in_notebook_file: Path to source notebook file.
        out_notebook_file: Path to output notebook file, after inserting metadata.
        in_metadata_file: Path to file with metadata to be added, in YAML format.
   """

    # %%
    with open(in_notebook_file, "r", encoding="utf8") as f:
        nb_json = json.load(f)

    # %% Reads the original notebook
    with open(in_metadata_file, "r", encoding="utf8") as f:
        in_metadata = yaml.safe_load(f)

    # %% Updates the notebook with the metadata
    for k, v in in_metadata.items():
        nb_json["metadata"][k] = v

    # %% Dumps the updated notebook
    with open(out_notebook_file, "w", encoding="utf8") as f:
        f.write(
            json.dumps(nb_json, indent=2, ensure_ascii=False)
        )


def notebook2pdf(in_notebook_filename):
    """Exports .ipynb notebook file to PDF

    Args:
        in_notebook_filename: Path to notebook file to convert.
    """

    in_notebook_filename = Path(in_notebook_filename)
    out_pdf_filename = in_notebook_filename.with_suffix('.pdf')

    with open(in_notebook_filename, "r", encoding="utf8") as f:
        nb = nbformat.read(f, as_version=4)

    #ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    #ep.preprocess(nb, {'metadata': {'path': '.'}})

    pdf_exporter = PDFExporter()
    pdf_data, _ = pdf_exporter.from_notebook_node(nb)

    with open(out_pdf_filename, "wb") as f:
        f.write(pdf_data)


@click.command()
@click.argument("source", type=click.Path(exists=True, dir_okay=False), nargs=1)
@click.argument("metadata", type=click.Path(exists=True, dir_okay=False), nargs=1)
@click.argument("destination", type=click.Path(), required=False, nargs=1)
def cli(source, metadata, destination=None):
    """This script adds metadata to a .ipynb notebook file, so that it
    can be properly rendered as PDF with article-type format 
    (typically, using `nbconvert --to pdf notebook.ipynb`).

    \b
    SOURCE:
        Original notebook file.

    \b
    METADATA:
        YAML file with the metadata to be added to the notebook.

    \b
    DESTINATION (optional):
        Output notebook file with added metadata.
        If not specified, SOURCE file is overwritten.
    """

    # If destination is empty, overwrites source
    if destination is None:
        destination = source

    # Adds metadata
    click.echo(f"Adding metadata from `{metadata}` to `{source}` (writing to `{destination}`)...")
    add_metadata(source, destination, metadata)

    # Converts to PDF
    click.echo(f"Exporting {destination} to PDF...")
    notebook2pdf(destination)

    click.echo("\nDONE")



# MAIN
if __name__ == '__main__':
    # %%
    cli()
