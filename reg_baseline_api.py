from fastapi import FastAPI
from fastapi.responses import StreamingResponse

import subprocess
import os
from typing import Union, Literal, Optional
from pathlib import Path
# from glob import glob
# from collections import defaultdict
# import json
from pydantic import BaseModel, field_validator, Field
