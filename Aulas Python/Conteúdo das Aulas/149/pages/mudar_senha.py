#!/Anaconda3/python
# -*- coding: UTF-8 -*-

__author__ = 'pedro'


def main(form, session):
    html = """
            <link href="css/registrar.css" rel="stylesheet"/>
            <h1 class="well">Cadastre sua Nova Senha</h1>
            <div class="col-lg-12 well">
    """

    if session.get('mudar_senha_state') != "":
        if session.get('mudar_senha_state') == "Sucesso":
            html += """
                <div class="alert alert-success alert-block fade in" id="successAlert">
                    <button class="close" type="button" data-dismiss="alert">&times;</button>

                    <h4>Sucesso!</h4>
                    <p>%s</p>
                </div>
            """ % session.get("mudar_senha_message")
        else:
            html += """
                <div class="alert alert-danger alert-block fade in" id="successAlert">
                    <button class="close" type="button" data-dismiss="alert">&times;</button>

                    <h4>Erro</h4>
                    <p>%s</p>
                </div>
            """ % session.get("mudar_senha_message")

    html += """
                <div class="row">
                    <form action="cgi-bin/MudaSenha.py" method="post" id="myForm">
                        <div class="col-sm-12">
                            <div class="row">
                                <!-- Nome de Usuário -->
                                <div class="col-sm-12 form-group">
                                    <label>Login</label>
                                    <input type="text" id="tLogin" name="cLogin"
                                           class="form-control" disabled="disabled"
                                           value='"""

    html += session.get("usuario")["usuario_login"] + """'/>
                                </div>
                            </div>

                                <!-- Senha Nova -->
                            <div class="row">
                                <div class="col-sm-12 form-group">
                                    <label>Nova Senha</label>
                                    <input type="password" id="tSenha1" name="cSenha1" placeholder="Nova Senha" class="form-control"
                                           value='"""

    html += session.get("mudar_senha_senha") + """'/>
                                </div>
                            </div>

                                <!-- Confirmar Nova Senha -->
                            <div class="row">
                                <div class="col-sm-12 form-group">
                                    <label>Confirmar Nova Senha</label>
                                    <input type="password" id="tSenha2" name="cSenha2" placeholder="Confirmar Nova Senha"
                                           class="form-control"
                                           value='"""

    html += session.get("mudar_senha_confsenha") + """'>
                                </div>
                            </div>

                            <hr/>

                            <div class="pull-right">
                                <button type="submit" class="btn btn-lg btn-primary" name="bSave">Salvar</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
    """

    return html
