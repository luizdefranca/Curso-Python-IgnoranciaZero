__author__ = 'pedro'


def main(panel_title, column_titles, column_names, page, rows, limit, dictionary, edit, table_info, page_redirect):
    html = """
            <div class="row">
                <div class="panel panel-primary filterable table-responsive">
                    <div class="panel-heading">
                        <h3 class="panel-title">""" + panel_title + """</h3>
                    </div>

                    <table class="table table-bordred table-striped">
                        <thead>
                            <tr>
    """
    for title in column_titles:
        html += "<th>" + title + """</th>
        """
    html += """
                             </tr>
                        </thead>

                        <tbody>
    """

    # With the limit selected we can start to fill the values on the table
    for i in range((page - 1)*rows, limit):
        fields_holder = {}

        html += """
                            <tr>
        """

        # We go throw each column name to select the proper table info
        for name in column_names:
            # First we add the property to the fields holder
            fields_holder[name] = table_info[i][name]

            # If the table info is empty we output an empty cell
            if table_info[i][name] == "" or table_info[i][name] is None:
                html += """
                                <td></td>
                """
                continue

            # For some tables we must get the equivalent string value to the
            # integer selected
            if name in dictionary:
                # To do so we look into the table data for the row in which
                # the primary key (FK on the mandado table) is
                for data_array in dictionary[name][0]:
                    if data_array[dictionary[name][1]] == table_info[i][name]:
                        # Once its found we echo the wanted column
                        html += """
                                <td>""" + data_array[dictionary[name][2]] + """</td>
                        """
                        break
            else:
                # Otherwise we just echo the table data
                html += """
                                <td>""" + str(table_info[i][name]) + """</td>
                """

        # If this table has a columns edit
        if edit:
            # We start to creating the form
            html += """
                                <td>
                                    <form action=""" + page_redirect + """ method="post">
            """

            # Then we set the hidden input values
            for (name, data) in fields_holder:
                html += """
                                        <input type="hidden" name='""" + name + """' value='""" + data + """'/>
                """

            # And finally set the edit button
            html += """
                                        <button type="submit" class="btn btn-default glyphicon glyphicon-pencil"></button>
                                    </form>
                                </td>
            """

        html += """
                            </tr>
        """

    html += """
                        </tbody>
                    </table>
                </div>
            </div>
    """

    return html
