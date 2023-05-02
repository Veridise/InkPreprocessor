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
python3 summarizer.py <PATH_TO_METADATA_JSON>
```

where `<PATH_TO_METADATA_JSON>` is the path to the `metadata.json` file created when using `cargo contract` to build an ink! contract.