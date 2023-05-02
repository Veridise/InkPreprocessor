# InkPreprocessor

The InkPreprocessor generates a JSON summary of a given ink! contract, which will be used by Vanguard.

## Requirements

- Python
- ink! (versions tested: 4.1.0, 4.2.0)
  - other versions may still work
  - only required for generating the metadata

## Usage

To generate a summary, run the following command:

```bash
python3 inkutils/summarizer.py <PATH_TO_METADATA_JSON>
```

where `<PATH_TO_METADATA_JSON>` is the path to the `metadata.json` file created when using `cargo contract` to build an ink! contract.

## Installation

This will install the summarizer into your current Python environment:

```bash
pip install .
```

Then you can use `ink-summarizer` anywhere by:

```bash
ink-summarizer <PATH_TO_METADATA_JSON>
```

To remove it, simply do:

```bash
pip uninstall inkutils
```

