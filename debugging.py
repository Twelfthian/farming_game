def debug_print(text:str, **kwargs):
    print(f"\x1b[38;2;0;0;255mDEBUG: \x1b[38;2;255m{text}\x1b[0m", **kwargs)