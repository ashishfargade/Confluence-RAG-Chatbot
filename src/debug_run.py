import logging
import sys
from streamlit import cli as stcli

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "streamlit.py"]
    sys.exit(stcli.main())