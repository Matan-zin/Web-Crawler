TAGS_WITHOUT_CLOSE : list[str] = [

    'br',
    'hr',
    'col',
    'img',
    'wbr',
    'link',
    'base',
    'area',
    'meta',
    'embed',
    'input',
    'param',
    'track',
    'keygen',
    'source',

] 


def is_has_close(name: str):

    return not name in TAGS_WITHOUT_CLOSE