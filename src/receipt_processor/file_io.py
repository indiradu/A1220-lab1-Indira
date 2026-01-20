# file_io.py
import os
import base64

def encode_file(path):
    """Encode a file as a base64 string.

    Args:
        path: Path to the file.

    Returns:
        Base64-encoded contents of the file.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def list_files(dirpath):
    """List files in a directory.

    Args:
        dirpath: Path to the directory.

    Yields:
        Tuples of (filename, full_path) for each file in the directory.
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path

