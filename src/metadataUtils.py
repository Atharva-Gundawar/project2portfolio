import subprocess


def geturl() -> str:
    """Returns remote github url

    Returns:
        str: url
    """
    return subprocess.run('git config --get remote.origin.url'.split(" "),
                            stdout=subprocess.PIPE).stdout.decode('utf-8')
                    
