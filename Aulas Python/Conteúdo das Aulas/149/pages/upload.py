#!/Anaconda3/python
# -*- coding: UTF-8 -*-

__author__ = 'pedro'


def main(form, session):
    html = """
            <link href="css/registrar.css" rel="stylesheet"/>
            <h1 class="well">Upload</h1>
            <div class="col-lg-12 well">
    """

    if session.get("upload_status") != "":
        if session.get("upload_status") == "Sucesso":
            html += """
                            <div class="alert alert-success alert-block fade in" id="successAlert">
                                <button class="close" type="button" data-dismiss="alert">&times;</button>
                                <h4>Sucesso!</h4>
                                <p>""" + session.get("upload_message") + """</p>
                            </div>
            """
        else:
            html += """
                            <div class="alert alert-danger alert-block fade in" id="successAlert">
                                <button class="close" type="button" data-dismiss="alert">&times;</button>
                                <h4>Erro</h4>
                                <p>""" + session.get("upload_message") + """</p>
                            </div>
            """

    html += """
                <div class="row">
                    <form action="cgi-bin/Upload.py" enctype="multipart/form-data" method="post" id="myForm">
                        <div class="col-sm-12">
                            <div class="row">
                                <div class="col-sm-12 form-group">
                                    <label>Arquivo</label>
                                    <input name="cFile" type="file" required/>
                                </div>
                            </div>

                            <hr/>
                            <button type="submit" class="btn btn-lg btn-primary pull-right bSubmit" name="bUp" value="submit">Upload</button>
                        </div>
                    </form>
                </div>
            </div>
    """

    return html
