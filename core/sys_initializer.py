import time

from PyQt6.QtCore import QObject, pyqtSignal


class SysInit(QObject):
    progress = pyqtSignal(int, str)
    finished = pyqtSignal()

    def run(self):
        steps = [
            "Loading configuration file...(1/10)",
            "Loading application files...(2/10)",
            "Calculate memory usage...(3/10)",
            "Check valid hardware...(4/10)",
            "Check licenses...(5/10)",
            "Initializing system...(6/10)",
            "Loading application...(7/10)",
            "Connecting to database...(8/10)",
            "Connecting to devices...(9/10)",
            "Joining home window...(10/10)",
        ]

        total = len(steps)

        for i, step in enumerate(steps):
            time.sleep(1)
            progress_value = int((i + 1) / total * 100)
            self.progress.emit(progress_value, step)

        self.finished.emit()