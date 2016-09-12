import os

__author__ = 'pedro'


def main(form, session):
    html = ""

    path = os.path.join("data", session.get("usuario")['usuario_login'])
    l = os.listdir(path)
    l.sort()
    for s in l:
        p = os.path.join(path, s).replace(os.sep, "/")
        if os.path.isfile(p) and 'cgi' in s:
            html += '<p><a href=%s> %s </a></p>\n' % (p, s)
    html += '<HR>'

    return html

