#!/usr/bin/env python3
"""Post-registration launcher; delegates to the byte-identical registered runner.
Keep the four scientific source files in this directory. No equations, inputs,
classification rules or stopping criteria are changed by this launcher.
"""
from pathlib import Path
import runpy
if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().with_name("UDCT_v7_12_Preregistration_Jeans_Transition.py")), run_name="__main__")
