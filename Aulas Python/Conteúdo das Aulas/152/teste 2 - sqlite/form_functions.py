__author__ = 'pedro'


def form(cgi_form):
    return {key: cgi_form[key].value for key in cgi_form}