import cgi

from paste.urlparser import PkgResourcesParser
from pylons.middleware import error_document_template
from webhelpers.html.builder import literal

from dactionsengine.lib.base import BaseController, render

class ErrorController(BaseController):
    """Generates error documents as and when they are required.

    The ErrorDocuments middleware forwards to ErrorController when error
    related status codes are returned from the application.

    This behaviour can be altered by changing the parameters to the
    ErrorDocuments middleware in your config/middleware.py file.

    """
    def document(self):
        """Render the error document"""

        request = self._py_object.request
        resp = request.environ.get('pylons.original_response')

        content = literal(resp.body) or cgi.escape(request.GET.get('message', ''))
        page = error_doc % \
            dict(prefix=request.environ.get('SCRIPT_NAME', ''),
                 code=cgi.escape(request.GET.get('code', str(resp.status_int))),
                 message=content)
        return page

    def img(self, id):
        """Serve Pylons' stock images"""
        return self._serve_file('/'.join(['media/img', id]))

    def style(self, id):
        """Serve Pylons' stock stylesheets"""
        return self._serve_file('/'.join(['media/style', id]))

    def _serve_file(self, path):
        """Call Paste's FileApp (a WSGI application) to serve the file
        at the specified path
        """
        request = self._py_object.request
        request.environ['PATH_INFO'] = '/%s' % path
        return PkgResourcesParser('pylons', 'pylons')(request.environ, self.start_response)

# ugly hack because I cannot get the error template to work
error_doc = literal("""\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
 <title>Server Error %(code)s</title>
 <link rel="stylesheet" href="%(prefix)s/styles.css" type="text/css" media="screen" />
</head>

<body>

	<div class="contents_wrapper">
		<div class="contents">
			<h3>Manifesto</h3>
			<p>
				We &hearts; design meet-ups to mingle and network, to inspire and being inspired. But we miss variety
				in topics and activities. In our daily project routines we dread for creative interruptions and small challenges
				to keep our minds nimble. Therefore working an evening on out-of-context challenge with new faces is sheer bliss.
			</p>
		</div>
	</div>

    <div id="banner">
        <div class="contents_wrapper">
            <div class="contents">
                <h1>%(code)s</h1>
                <h2>We cannot find what you are looking for. Sorry. :{<br/>&nbsp;</h2>
				<h3>Contact</h3>
				<p>
					Twitter: <a href="http://twitter.com/#!/DActions" name="Link to DActions on Twitter"> @DActions</a>
					&nbsp;&nbsp;&times;&nbsp;&nbsp;Facebook: <a href="http://www.facebook.com/groups/DActions.SG" name="Link to DActions on Facebook"> DActions.SG</a>
					&nbsp;&nbsp;&times;&nbsp;&nbsp;e-Mail:
					<a href="mailto:info@dactions.org" name="e-mail to DActions"> info@dactions.org</a>
				</p>
            </div>
        </div>
    </div>

</body>
</html>
""")