# coding: utf-8
import shelve

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    """ $BEj9F%G!<%?$rJ]B8$7$^$9(B
    """
    # shelve$B%b%8%e!<%k$G%G!<%?%Y!<%9%U%!%$%k$r3+$-$^$9(B
    database = shelve.open(DATA_FILE)
    # $B%G!<%?%Y!<%9$K(Bgreeting_list$B$,$J$1$l$P!"?7$7$/%j%9%H$r:n$j$^$9(B
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        # $B%G!<%?%Y!<%9$+$i%G!<%?$r<hF@$7$^$9(B
        greeting_list = database['greeting_list']
    # $B%j%9%H$N@hF,$KEj9F%G!<%?$rDI2C$7$^$9(B
    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'create_at': create_at,
        })
    # $B%G!<%?%Y!<%9$r99?7$7$^$9(B
    database['greeting_list'] = greeting_list
    # $B%G!<%?%Y!<%9%U%!%$%k$rJD$8$^$9(B
    database.close()

def load_data():
    """ $BEj9F$5$l$?%G!<%?$rJV$7$^$9(B
    """
    # shelve$B%b%8%e!<%k$G%G!<%?%Y!<%9%U%!%$%k$r3+$-$^$9(B
    database = shelve.open(DATA_FILE)
    # greeting_list$B$rJV$7$^$9!#%G!<%?$,$J$1$l$P6u$N%j%9%H$rJV$7$^$9(B
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list

