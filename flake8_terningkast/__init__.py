import math
import subprocess # noqa B404

from flake8.formatting import base

from .dice import dice1, dice2, dice3, dice4, dice5, dice6


class TerningkastPlugin(base.BaseFormatter):
    """Terninkast code rater."""

    name = "terningkast"
    version = "1.0"
    error_format = '%(path)s:%(row)d:%(col)d: %(code)s %(text)s'

    def after_init(self):
        """Initialize the plugin."""
        cmd = "git diff --stat HEAD"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE) # noqa B602
        process.wait()
        if process.returncode:
            raise Exception("No git repo detected")

        stdout = process.stdout.read().decode()
        self.errors = 0
        if stdout == "":
            self.changes = 0
        else:
            # Parse the changes out of the git diff
            # And set to 0 if no changes are found
            stats = stdout.splitlines()[len(stdout.splitlines())-1]

            if "+" in stats.split(",")[1]:
                self.changes = int(stats.split(",")[1].split(" ")[1])
            else:
                self.changes = 0

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
        print("\n"*4)
        print(f"Changes: {self.changes}")
        print(f"Errors: {self.errors}")
        print("And your Terningkast is:")
        if self.errors == 0 or self.changes == 0:
            dice6()
        else:
            terningkast = 6-math.ceil(((self.errors/self.changes)*100)/16.5)
            if terningkast == 1:
                dice1()
            elif terningkast == 2:
                dice2()
            elif terningkast == 3:
                dice3()
            elif terningkast == 4:
                dice4()
            elif terningkast == 5:
                dice5()
            elif terningkast == 6:
                dice6()
