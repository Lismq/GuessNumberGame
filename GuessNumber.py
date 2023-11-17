from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
import sys
import random

class GuessNumberGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

        self.secret_number = random.randint(1,100)

        self.attempts = 0
        self.max_attempts = 5

    def init_ui(self):
        self.label = QLabel("Введите число:")
        self.line_edit = QLineEdit()
        self.button = QPushButton('Проверить')
        self.result_label = QLabel('Попробуйте угадать число!')


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        self.button.clicked.connect(self.check_guess)

        self.setWindowTitle("Угадай число!")
        self.setGeometry(100,100,400,300)


    def format_attempts(self, attempts):
        if attempts % 10 == 1 and attempts % 100 != 11:
            return f'{attempts} попытка'
        elif 2 <= attempts % 10 <= 4 and (attempts % 100 < 10 or attempts % 100 >= 20):
            return f'{attempts} попытки'
        else:
            return f'{attempts} попыток'


    def check_guess(self):
        try:
            guess = int(self.line_edit.text())
            self.attempts += 1

            if guess == self.secret_number:
                self.show_message('Поздравляем!', f'Вы угадали число за {self.format_attempts(self.attempts)}!')
                self.reset_game()
            else:
                hint = self.get_hint(guess)
                self.result_label.setText(hint)

                if self.attempts == self.max_attempts:
                    self.show_message('Игра окончена', f'Вы использовали все {self.format_attempts(self.max_attempts)}. Загаданное число: {self.secret_number}')
                    self.reset_game()
        except ValueError:
            self.result_label.setText('Введите корректное число!')


    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.setText('Попробуйте угадать число!')

    def show_message(self, title, text):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.exec()

    def get_hint(self, guess):
        difference = abs(self.secret_number - guess)

        if difference == 0:
            return 'Вы угадали число!'
        elif difference <= 5:
            return f'Очень горячо! У вас осталось {self.format_attempts(self.max_attempts-self.attempts)}, попробуйте еще раз.'
        elif difference <= 10:
            return f'Горячо! У вас осталось {self.format_attempts(self.max_attempts-self.attempts)}, попробуйте еще раз.'
        elif difference <= 20:
            return f'Тепло! У вас осталось {self.format_attempts(self.max_attempts-self.attempts)}, попробуйте еще раз.'
        else:
            return f'Холодно! У вас осталось {self.format_attempts(self.max_attempts-self.attempts)}, попробуйте еще раз.'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GuessNumberGame()
    game.show()
    sys.exit(app.exec())