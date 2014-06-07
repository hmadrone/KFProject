from pyramid.response import Response
from pyramid.view import (
    view_config,
    view_defaults
)

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_KFProject_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

@view_defaults()
class KFViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='templates/homebody.pt')
    def home(self):
        try:
            one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
        except DBAPIError:
            return Response(conn_err_msg, content_type='text/plain', status_int=500)
        return {'one': one, 'project': 'KFProject', 'view': 'home'}

    @view_config(route_name='style', renderer='templates/style.pt')
    def style(self):
        try:
            one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
        except DBAPIError:
            return Response(conn_err_msg, content_type='text/plain', status_int=500)
        return {'one': one, 'project': 'KFProject', 'view': 'style'}

    @view_config(route_name='size', renderer='templates/size.pt')
    def size(self):
        try:
            one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
        except DBAPIError:
            return Response(conn_err_msg, content_type='text/plain', status_int=500)
        return {'one': one, 'project': 'KFProject', 'view': 'size'}

    @view_config(route_name='yarn', renderer='templates/yarn.pt')
    def yarn(self):
        try:
            one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
        except DBAPIError:
            return Response(conn_err_msg, content_type='text/plain', status_int=500)
        return {'one': one, 'project': 'KFProject', 'view': 'yarn'}



