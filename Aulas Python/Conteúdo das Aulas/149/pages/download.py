#!/Anaconda3/python
# -*- coding: UTF-8 -*-

__author__ = 'pedro'


def main(form, session):
    html = """
            <link href="css/registrar.css" rel="stylesheet"/>
            <h1 class="well">Download</h1>
            <div class="col-lg-12 well">
                <div class="row">
                    <form action="cgi-bin/Download.py" method="post" id="myForm">
                        <div class="col-sm-12">
                            <div class="row">
                                <div class="col-sm-12 form-group">
                                    <label>Arquivos</label>
                                    <div class="controls">
                                        <select id="tArq" name="cArq" class="form-control">
                                            <option value="">-Selecione-</option>"""

    for i in range(len(session.get("arquivos"))):
        if ".py" in session.get("arquivos")[i]:
            html += """
                                            <option value="%i">%s</option>""" % (i, session.get("arquivos")[i])

    html += """
                                        </select>
                                    </div>
                                </div>
                            </div>

                            <hr/>
                            <button type="submit" class="btn btn-lg btn-primary pull-right bSubmit" name="bDown" value="submit">Download</button>
                        </div>
                    </form>
                </div>
            </div>
    """

    return html
