# logic.py
import os, csv
from PyQt6.QtWidgets import QMainWindow, QLineEdit
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt
from gui import Ui_MainWindow

CSV_FILE = "grades.csv"

class GradesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Student Grades")

        # restrict attempts to 1..4 in the line edit
        self.ui.attemptsEdit.setPlaceholderText("1–4")
        self.ui.attemptsEdit.setValidator(QIntValidator(1, 4, self))

        self.score_edits = []

        # rebuild scores whenever attempts changes
        self.ui.attemptsEdit.textChanged.connect(self._attempts_changed)

        # submit handler
        self.ui.submitButton.clicked.connect(self.handle_submit)

        # initial state (default to 2 if empty)
        if not self.ui.attemptsEdit.text().strip():
            self.ui.attemptsEdit.setText("2")
        self.build_score_inputs(self._get_attempts())

    # ---- helpers ----
    def _attempts_changed(self):
        n = self._get_attempts(silent=True)
        self.build_score_inputs(n)

    def _get_attempts(self, silent=False) -> int:
        t = self.ui.attemptsEdit.text().strip()
        if t.isdigit():
            n = int(t)
            if 1 <= n <= 4:
                return n
        if not silent:
            self.show_status("Attempts must be an integer from 1 to 4.", "error")
        return 2

    def build_score_inputs(self, n: int):
        # clear current
        for e in self.score_edits:
            e.deleteLater()
        self.score_edits.clear()

        # create n score edits
        for i in range(1, n + 1):
            edit = QLineEdit(self)
            edit.setObjectName(f"score{i}Edit")
            edit.setPlaceholderText(f"Score {i} (0–100)")
            edit.setMaxLength(3)
            edit.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.ui.scoresLayout.addWidget(edit)
            self.score_edits.append(edit)

        self.show_status(f"Enter {n} score(s).", "info")

    def show_status(self, text: str, kind: str = "info"):
        color = {"ok": "#2e7d32", "error": "#c62828", "info": "#ef6c00"}.get(kind, "#ef6c00")
        self.ui.statusLabel.setStyleSheet(f"color:{color};")
        self.ui.statusLabel.setText(text)

    # ---- validation + save ----
    def validate(self):
        name = self.ui.nameEdit.text().strip()
        if not name:
            self.show_status("Name cannot be empty.", "error")
            return None

        attempts = self._get_attempts()
        scores = []
        for i, e in enumerate(self.score_edits, start=1):
            t = e.text().strip()
            if t == "":
                self.show_status(f"Score {i} is empty.", "error"); return None
            try:
                v = float(t)
            except ValueError:
                self.show_status(f"Score {i} must be a number.", "error"); return None
            if not (0 <= v <= 100):
                self.show_status(f"Score {i} must be between 0 and 100.", "error"); return None
            scores.append(v)

        if len(scores) != attempts:
            self.show_status("Attempts and number of scores don’t match.", "error"); return None
        return name, attempts, scores

    def handle_submit(self):
        ok = self.validate()
        if not ok: return
        name, attempts, scores = ok
        highest, lowest = max(scores), min(scores)
        average = round(sum(scores)/len(scores), 2)
        padded = scores + ["", "", "", ""]

        row = {
            "name": name, "attempts": attempts,
            "score1": padded[0], "score2": padded[1],
            "score3": padded[2], "score4": padded[3],
            "highest": round(highest,2), "lowest": round(lowest,2),
            "average": average,
        }
        newfile = not os.path.exists(CSV_FILE)
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(row.keys()))
            if newfile: w.writeheader()
            w.writerow(row)
        self.show_status("Submitted — saved to grades.csv ✔", "ok")
