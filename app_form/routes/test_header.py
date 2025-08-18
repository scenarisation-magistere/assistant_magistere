from flask import render_template

def init_test_routes(app):
    @app.route('/test-header')
    def test_header():
        return render_template('test_header_fix.html')
