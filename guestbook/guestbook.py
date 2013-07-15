# coding: utf-8
import shelve
from datetime import datetime
from flask import Flask, request, render_template, redirect, escape, Markup

application = Flask(__name__)

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

@application.route('/')
def index():
    """ $B%H%C%W%Z!<%8(B
    $B%F%s%W%l!<%H$r;HMQ$7$F%Z!<%8$rI=<($7$^$9(B
    """
    # $BEj9F%G!<%?$rFI$_9~$_$^$9(B
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)

@application.route('/post', methods=['POST'])
def post():
    """ $BEj9FMQ(BURL
    """
    # $BEj9F$5$l$?%G!<%?$r<hF@$7$^$9(B
    name = request.form.get('name') # $BL>A0(B
    comment = request.form.get('comment') # $B%3%a%s%H(B
    create_at = datetime.now() # $BEj9FF|;~!J8=:_;~4V!K(B
    # $B%G!<%?$rJ]B8$7$^$9(B
    save_data(name, comment, create_at)
    # $BJ]B88e$O%H%C%W%Z!<%8$K%j%@%$%l%/%H$7$^$9(B
    return redirect('/')

@application.template_filter('nl2br')
def nl2br_filter(s):
    """ $B2~9TJ8;z$r(Bbr$B%?%0$KCV$-49$($k%F%s%W%l!<%H%U%#%k%?(B
    """
    return escape(s).replace('\n', Markup('<br />'))

@application.template_filter('datetime_fmt')
def datatime_fmt_filter(dt):
    """ datettime$B%*%V%8%'%/%H$r8+$d$9$$I=<($K$9$k%F%s%W%l!<%H%U%#%k%?(B
    """
    return dt.strftime('%Y/%m/%d %H:%M:%S')

if __name__ == '__main__':
    # IP$B%"%I%l%9(B127.0.0.1$B$N(B5000$BHV%]!<%H$G%"%W%j%1!<%7%g%s$r<B9T$7$^$9(B
    application.run('127.0.0.1', 5000, debug=True)
