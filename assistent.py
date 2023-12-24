"""
Liste mit Custom GPTs
"""

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

gpts = {
    "kirenz": os.getenv('OPENAI_ASSISTANT'),
    "ContentCrafter": os.getenv('ContentCrafter'),
    "PersonaTutor": os.getenv('PersonaTutor')
}