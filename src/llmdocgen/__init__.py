"""
Library for reading and writing trigger files.
"""

__version__ = "0.1.0"


def get_version():
    """
    Get the version of the library
    :return: Full Version String
    """
    return __version__


if __name__ == '__main__':
    # Module execution support
    from . import executor

    executor.main()
