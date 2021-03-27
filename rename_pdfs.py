import re
import os

files = [f for f in os.listdir("pdf") if f.endswith(".pdf")]


def clear_name(f: str) -> str:
    if "(" in f:
        return (re.findall(r"\((\d+)\)", f)[0]+".pdf").zfill(7)
    else:
        try:
            return re.findall(r"\d+", f)[0]+".pdf".zfill(7)
        except IndexError:
            return f


{f:clear_name(f) for f in files}
