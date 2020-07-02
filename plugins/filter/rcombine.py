import itertools
from functools import reduce

from ansible.module_utils.six import iteritems
from ansible.errors import AnsibleFilterError
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.utils.vars import merge_hash
from ansible.plugins.filter.core import combine


def rcombine(*terms, **kwargs):
    recursive = kwargs.get('recursive', False)
    if len(kwargs) > 1 or (len(kwargs) == 1 and 'recursive' not in kwargs):
        raise AnsibleFilterError("'recursive' is the only valid keyword argument")

    dicts = []
    for t in terms:
        if isinstance(t, MutableMapping):
            dicts.append(t)
        elif isinstance(t, list):
            dicts.append(combine(*t, **kwargs))
        else:
            raise AnsibleFilterError("|combine expects dictionaries, got " + repr(t))

    dicts.reverse()

    if recursive:
        return reduce(merge_hash, dicts)
    else:
        return dict(itertools.chain(*map(iteritems, dicts)))


class FilterModule(object):

    def filters(self):
        return {
            'rcombine': rcombine,
        }
