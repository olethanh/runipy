import os


def export(name, content):
    if "NB_FILES_EXPORT_PATH" not in os.environ:
        return

    open(os.path.join(os.environ["NB_FILES_EXPORT_PATH"], name), "w").write(content)
