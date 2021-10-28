import time


class ProgressBar:

    def __init__(self, steps: int = 5, bar_length: int = 60, bar_name: str = "Сканер портов"):
        """
        Конструктор Progress Bar
        :param steps: кол-во шагов
        :param bar_length: длина в консоле
        """

        self.steps = steps
        self.bar_length = bar_length
        self.bar_name = bar_name
        self.progress_char = "█"
        self.fill_char = "░"
        self.start_time = None
        self.complete_status = False

    def calculate(self, current_value: int) -> None:
        """
        Пересчитывает progress bar
        :param current_value: текущее значение progress bar
        :return: None
        """

        if self.start_time is None:
            self.start_time = time.time()

        one_percent = current_value / float(self.steps)

        progress = f"{self.progress_char * int(one_percent * self.bar_length):{self.fill_char}{'<'}{self.bar_length}}"

        percent = f"{100 * one_percent:.1f}"

        progress_bar = f"{self.bar_name}: {current_value}/{self.steps} |{progress}| {percent}%"

        print(progress_bar, end='\r')

        if current_value >= self.steps:
            self.complete()

    def complete(self) -> None:
        """
        Вывод времени выполнения
        :return: None
        """

        if not self.complete_status:
            print(f"\nВремя выполнения составило {time.time() - self.start_time:.2f} секунду")
            self.start_time = None
            self.complete_status = True
