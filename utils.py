import os
from StringIO import StringIO


def export(name, content):
    if "/" in name:
        raise Exception("You aren't able to put a '/' in the filename")

    if not isinstance(name, basestring):
        raise Exception("The file name should be a string")

    if not isinstance(content, basestring):
        raise Exception("The file content should be a string")

    if "NB_FILES_EXPORT_PATH" not in os.environ:
        return

    open(os.path.join(os.environ["NB_FILES_EXPORT_PATH"], name), "w").write(content)


def output(name):
    if "/" in name:
        raise Exception("You aren't able to put a '/' in the filename")

    if not isinstance(name, basestring):
        raise Exception("The file name should be a string")

    if "NB_FILES_EXPORT_PATH" not in os.environ:
        return StringIO()

    return open(os.path.join(os.environ["NB_FILES_EXPORT_PATH"], name), 'wb')
