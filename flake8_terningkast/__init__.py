from flake8.formatting import base


class TerningkastPlugin(base.BaseFormatter):
    """Terninkast code rater"""
    name = "terningkast"
    version = "0.0.1"
    error_format = '%(path)s:%(row)d:%(col)d: %(code)s %(text)s'

    def after_init(self):
        """Initialize the plugin."""
        print("after init")
        self.errors = 0

    def handle(self, error):
        """Handle a single error."""
        line = self.format(error)
        source = self.show_source(error)
        self.write(line, source)
        self.errors += 1

    def format(self, error):
        """Must be overwritten."""
        # Default format for flake8
        return self.error_format % {
            "code": error.code,
            "text": error.text,
            "path": error.filename,
            "row": error.line_number,
            "col": error.column_number,
        }

    def stop(self):
        """Generate report(terningkast)."""
        print("BYE")
