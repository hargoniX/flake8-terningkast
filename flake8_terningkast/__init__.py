from flake8.formatting import base
from .dice import dice1, dice2, dice3, dice4, dice5, dice6

import subprocess


class TerningkastPlugin(base.BaseFormatter):
    """Terninkast code rater"""
    name = "terningkast"
    version = "0.0.1"
    error_format = '%(path)s:%(row)d:%(col)d: %(code)s %(text)s'

    def after_init(self):
        """Initialize the plugin."""
        cmd = "git diff --stat HEAD"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode:
            raise Exception("No git repo detected")

        stdout = process.stdout.read()
        print("stdout: "+stdout)
        if stdout == "":
            self.changes = 0
            return

        stats = stdout.splitlines()[len(stdout.splitlines())-1].decode()

        if "+" in stats.split(",")[1]:
            self.changes = stats.split(",")[1].split(" ")[1]
        else:
            self.changes = 0
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
