__author__ = 'pedro'


def main(pages, page, page_name):
    html = """
            <ul class="pagination pull-right">
    """

    if pages >= 5:
        # Otherwise first we must check if we are within the first five boxe
        # If the page is one of the firsts
        if page < 5:
            # First we set the left arrow to go to the previous page
            if page == 1:
                html += """
                            <li class="disabled">
                                <a href="#">
                                    <i class="glyphicon glyphicon-chevron-left"></i>
                                </a>
                            </li>
                """
            else:
                html += """
                            <li>
                                <a href='fetch_page.py?page=""" + page_name + """&i=""" + str(page - 1) + """'>
                                    <i class="glyphicon glyphicon-chevron-left"></i>
                                </a>
                            </li>
                """

            # If we are we just echo a few links together and the space link
            for i in range(5):
                if i != page - 1:
                    html += """
                            <li><a href='fetch_page.py?page=""" + page_name + """&i=""" + str(i + 1) + """'>""" + str(i + 1) + """</a></li>
                    """
                else:
                    html += """
                            <li class="active"><a href='fetch_page.py?page=""" + page_name + """&i=""" + str(i + 1) + """'>""" + str(i + 1) + """</a></li>
                    """

                # Then we insert the right arrow to switch page
                html += """
                            <li>
                                <a href=href='fetch_page.py?page=""" + page_name + """&i=""" + str(page + 1) + """'>
                                    <i class="glyphicon glyphicon-chevron-right"></i>
                                </a>
                            </li>
                """

        # If the page is in the middle
        elif 5 <= page < pages - 3:
            # First we set the arrow that goes back to the first page
            html += """
                            <li>
                                <a href=href='fetch_page.py?page=""" + page_name + """&i=1'>
                                        <i class="glyphicon glyphicon glyphicon-backward"></i>
                                </a>
                            </li>
            """

            # Then we set the arrow to the left
            html += """
                            <li>
                                <a href='fetch_page.py?page=""" + page_name + """&i=""" + str(page - 1) + """'>
                                    <i class="glyphicon glyphicon-chevron-left"></i>
                                </a>
                            </li>
            """

            # Then we put the buttons that go in the middle
            html += """
                        <li><a href='fetch_page.py?page=""" + page_name + """&i=""" + str(page - 1) + """'>""" + str(page - 1) + """</a></li>
                        <li class="active"><a href='fetch_page.py?page=""" + page_name + """&i=""" + str(page) + """'>""" + str(page) + """</a></li>
                        <li><a href='fetch_page.py?page=""" + page_name + """&i=""" + str(page + 1) + """'>""" + str(page + 1) + """</a></li>
            """

            # Then we insert the right arrow to switch page
            html += """
                            <li>
                                <a href='fetch_page.py?page=""" + page_name + """&i=""" + str(page + 1) + """'">
                                    <i class="glyphicon glyphicon-chevron-right"></i>
                                </a>
                            </li>
            """

            # And finally a double arrow to go to the last page
            html += """
                            <li>
                                <a href='fetch_page.py?page=""" + page_name + """&i=""" + str(pages) + """'">
                                        <i class="glyphicon glyphicon glyphicon-forward"></i>
                                </a>
                            </li>
            """

        # If the page is one of the last
        else:
            # First we set the arrow that goes back to the first page
            html += """
                            <li>
                                <a href='fetch_page.py?page=""" + page_name + """&i=1'>
                                        <i class="glyphicon glyphicon glyphicon-backward"></i>
                                </a>
                            </li>
            """

            # Then we set the arrow to the left
            html += """
                            <li>
                                <a href='fetch_page.py?page=""" + page_name + """&i=""" + str(page - 1) + """'>
                                    <i class="glyphicon glyphicon-chevron-left"></i>
                                </a>
                            </li>
            """

            # Then we put the lasts pages
            for i in range(pages - 5, pages):
                if i != page - 1:
                    html += """
                            <li><a href='fetch_page.py?page=""" + page_name + """&i=""" + str(i + 1) + """'>""" + str(i + 1) + """</a></li>
                    """
                else:
                    html += """
                            <li class="active"><a href='fetch_page.py?page=""" + page_name + """&i=""" + str(i + 1) + """'>""" + str(i + 1) + """</a></li>
                    """

            # Then we insert the right arrow to switch page
            if page != pages:
                html += """
                            <li>
                                <a href='fetch_page.py?page=""" + page_name + """&i=""" + str(page + 1) + """'>
                                    <i class="glyphicon glyphicon-chevron-right"></i>
                                </a>
                            </li>
                """
            else:
                html += """
                            <li class="disabled">
                                <a href="#">
                                    <i class="glyphicon glyphicon-chevron-right"></i>
                                </a>
                            </li>
                """
    else:
        # First we set the left arrow to go to the previous page
        if page == 1:
            html += """
                            <li class="disabled">
                                <a href="#">
                                    <i class="glyphicon glyphicon-chevron-left"></i>
                                </a>
                            </li>
            """
        else:
            html += """
                            <li>
                                <a href='fetch_page.py?page=""" + page_name + """&i=""" + str(page - 1) + """'>
                                    <i class="glyphicon glyphicon-chevron-left"></i>
                                </a>
                            </li>
            """

        # If we are we just echo a few links together and the space link
        for i in range(pages):
            if i != page - 1:
                 html += """
                            <li><a href='fetch_page.py?page=""" + page_name + """&i=""" + str(i + 1) + """'>""" + str(i + 1) + """</a></li>
                 """
            else:
                html += """
                            <li class="active"><a href='fetch_page.py?page=""" + page_name + """&i=""" + str(i + 1) + """'>""" + str(i + 1) + """</a></li>
                """

        # Then we insert the right arrow to switch page
        if pages > 1 and page != pages:
            html += """
                            <li>
                                <a href='fetch_page.py?page=""" + page_name + """&i=""" + str(page + 1) + """'">
                                    <i class="glyphicon glyphicon-chevron-right"></i>
                                </a>
                            </li>
            """
        else:
            html += """
                            <li class="disabled">
                                <a href="#">
                                    <i class="glyphicon glyphicon-chevron-right"></i>
                                </a>
                            </li>
            """
    html += """
            </ul>
    """

    return html
