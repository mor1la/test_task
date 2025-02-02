class HashTable:
    def __init__(self, size=10):
        """
        Инициализация хэш-таблицы.
        size: размер таблицы (количество ячеек).
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Хэш-функция для вычисления индекса в таблице.
        key: ключ, для которого вычисляется хэш.
        Возвращает индекс в таблице.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Вставка пары ключ-значение в хэш-таблицу.
        key: ключ.
        value: значение.
        Если ключ уже существует, его значение обновляется.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))

    def get(self, key):
        """
        Получение значения по ключу.
        key: ключ, для которого нужно получить значение.
        Возвращает значение, если ключ найден, иначе None.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None

    def delete(self, key):
        """
        Удаление пары ключ-значение по ключу.
        key: ключ, который нужно удалить.
        Если ключ не найден, ничего не происходит.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def __str__(self):
        """
        Возвращает строковое представление хэш-таблицы.
        Каждая ячейка выводится с его индексом и содержимым.
        """
        return '\n'.join([f'{i}: {bucket}' for i, bucket in enumerate(self.table)])

