import logging
import mwparserfromhell as mwp

from util import ftag
from client import Client
from models import WikiTable

logging.basicConfig(level=logging.WARN)
log = logging.getLogger('wikitables')


def import_tables(article, title, lang="en"):
    #title = re.search(r"<title>(.+)</title>", article).group(1)
    ## parse for tables
    raw_tables = mwp.parse(article).filter_tags(matches=ftag('table'))

    def _table_gen():
        for idx, table in enumerate(raw_tables):
            name = '%s[%s]' % (title,idx)
            yield WikiTable(name, table)

    return list(_table_gen())
