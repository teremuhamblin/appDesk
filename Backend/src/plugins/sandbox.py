import traceback

def sandbox_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print("[SANDBOX] Erreur isolée :", e)
        traceback.print_exc()
        return None
