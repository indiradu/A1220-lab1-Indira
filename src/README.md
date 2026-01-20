# Receipt Processing CLI

## Description
Python CLI that processes a directory of receipt images and extracts the receipt date, total amount, vendor name, and a category using the OpenAI API. Output is printed as a JSON dictionary keyed by filename.

## Structure
src/receipt_processor/   
├── init.py   
├── main.py  
├── file_io.py  
├── gpt.py

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key"

Run
make run
# or
python src/receipt_processor/main.py receipts --print
```
## Output
The program prints a JSON object mapping each receipt filename to the extracted information.

## License
MIT