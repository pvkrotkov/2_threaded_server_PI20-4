class P_Bar:

    def __init__(self, total, suffix='', fill='█', width=40):
        
        self._total = total #Количество операций, действий.
        self._fill = fill #Сообщение, выводимое перед баром.
        self._suffix = suffix #Символ-заполнитель.
        self._width = width #Количество символов, которое будет занимать бар (вес).

        self._current = 0
        self._unused_part = 0

    def __str__(self): #Возвращает строковое представление бара в текущем состоянии.
        bar = '\r'
        if self._suffix:
            bar += self._suffix + ' '
        filled = self._fill * self._fill_count
        empty = ' ' * self._empty_count
        bar += f'[{filled}{empty}]' + ' '
        bar += f'({self._current}/{self._total})' + ' '
        bar += f'{self._percentages}%'
        bar += '\r'
        if self.completed():
            bar += '\n'
        return bar

    def __len__(self): #Возвращает длину строкового представления бара в текущем состоянии.
        return len(str(self))

    def print(self): #Печатает бар, убирая символ переноса для поодержки печати на одной строке.
        print(self, end='')

    def update(self): #Переводит бар в следующее состояние и печатает его.
        self.next()
        self.print()

    def next(self): #Переводит бар в следующее состояние.
        if not self.completed():
            self._current += 1

    def completed(self): #Возвращает True, если бар находится в последнем возможном состоянии.
        return self._current == self._total

    @property
    def _completed_part(self): #Возвращает текущую долю завершенности всех операций.
        return self._current / self._total

    @property
    def _percentages(self): #Возвращает процент завершения всех операций.
        return round(self._completed_part * 100, 2)

    @property
    def _fill_count(self): #Возвращает кол-во символов, которое необходимо заполнить символом-заполнителем.
        to_fill = self._completed_part * self._width
        if self._unused_part > 0:
            fill_count = round(to_fill + self._unused_part)
        else:
            fill_count = round(to_fill)
        self.unused_part = fill_count - to_fill
        return fill_count

    @property
    def _empty_count(self): #Возвращает кол-во символов, которое необходимо заполнить символом-пустоты.
        return self._width - self._fill_count
