import time

from PyQt6.QtCore import QObject, pyqtSignal


class SysInit(QObject):
    progress = pyqtSignal(int, str)
    finished = pyqtSignal()

    def run(self):
        steps = [
            "Loading configuration file...(1/3)",
            "Loading application files...(2/3)",
            "Calculate memory usage...(3/3)"
        ]

        total = len(steps)

        for i, step in enumerate(steps):
            time.sleep(1)
            progress_value = int((i + 1) / total * 100)
            self.progress.emit(progress_value, step)

        self.finished.emit()