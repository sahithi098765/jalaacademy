try:
    import nonexistent_module  
except ModuleNotFoundError as e:
    print(f"ClassNotFoundException Occurred: {e}")
