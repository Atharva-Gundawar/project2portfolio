import subprocess


def getUrl() -> str:
    """Returns remote github url

    Returns:
        str: url
    """
    return subprocess.run('git config --get remote.origin.url'.split(" "),
                          stdout=subprocess.PIPE).stdout.decode('utf-8')


def colabUrl(url: str) -> str:
    """Returns colab url for a given ipynb notebook hosted on github

    Args:
        url (str): ipynb github url

    Returns:
        str: colab url
    """

    return 'http://colab.research.google.com/github/' + url[19:]
