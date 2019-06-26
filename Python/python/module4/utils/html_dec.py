def bold(fn):
    def wrapped():
        return "<b>" + str(fn()) + "</b>"

    return wrapped


def italic(fn):
    def wrapped():
        return "<i>" + str(fn()) + "</i>"

    return wrapped


def underline(fn):
    def wrapped():
        return "<u>" + str(fn()) + "</u>"

    return wrapped
