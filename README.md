# Отборочное задание
[Условие задания](https://docs.google.com/document/d/19vqmV_AsfxY695s5fv6PwCo3f5-o95QcYDFcTRKSoWY/edit?tab=t.0) 
# Проект: Реализация АВЛ-дерева и хеш-таблицы на Python

## Описание
Этот репозиторий содержит две независимые реализации структур данных:
1. **АВЛ-дерево** (сбалансированное двоичное дерево поиска)
2. **Хеш-таблица** (ассоциативный массив с методом цепочек)

Каждая структура данных реализована в отдельной директории: `task1` (AVL-дерево) и `task2` (хеш-таблица).

---

## Структура репозитория
```
.
├── task1               # Реализация AVL-дерева
│   ├── AVLNode.py      # Класс узла AVL-дерева
│   ├── AVLTree.py      # Класс AVL-дерева и основные операции
│   ├── DrawTree.py     # Визуализация дерева
│   ├── test.py         # Тесты для AVL-дерева (pytest)
│   └── readme.md       # Описание реализации AVL-дерева
│
├── task2               # Реализация хеш-таблицы
│   ├── HashTable.py    # Класс хеш-таблицы
│   ├── test.py         # Тесты для хеш-таблицы (pytest)
│   └── readme.md       # Описание реализации хеш-таблицы
│
├── README.md           # Этот файл
└── requirements.txt    # Список зависимостей
```
---

## Запуск тестов
Тесты написаны с использованием `pytest`. Для их запуска выполните команду:
```
pytest task1/test.py  # Для AVL-дерева
pytest task2/test.py  # Для хеш-таблицы
```

---

## Установка зависимостей
Перед использованием установите необходимые зависимости:
```
pip install -r requirements.txt
```

---
