import pytest
from HashTable import HashTable

def test_insert_and_get():
    ht = HashTable()
    ht.insert("apple", 5)
    ht.insert("banana", 10)
    
    assert ht.get("apple") == 5
    assert ht.get("banana") == 10
    assert ht.get("orange") is None

def test_insert_update():
    ht = HashTable()
    ht.insert("apple", 5)
    ht.insert("apple", 10)
    
    assert ht.get("apple") == 10

def test_delete():
    ht = HashTable()
    ht.insert("apple", 5)
    ht.insert("banana", 10)
    
    ht.delete("apple")
    assert ht.get("apple") is None
    assert ht.get("banana") == 10

def test_delete_nonexistent_key():
    ht = HashTable()
    ht.insert("apple", 5)
    
    ht.delete("banana")  # Удаление несуществующего ключа
    assert ht.get("apple") == 5

def test_collision_handling():
    ht = HashTable(size=1)  # Все ключи будут попадать в однe ячейку (проверка решения коллизий)
    ht.insert("apple", 5)
    ht.insert("banana", 10)
    
    assert ht.get("apple") == 5
    assert ht.get("banana") == 10

def test_empty_table():
    ht = HashTable()
    
    assert ht.get("apple") is None
    ht.delete("apple")  # Удаление из пустой таблицы

def test_large_table():
    ht = HashTable(size=100)
    for i in range(1000):
        ht.insert(f"key{i}", i)
    
    assert ht.get("key0") == 0
    assert ht.get("key999") == 999
    assert ht.get("key1000") is None

def test_string_representation():
    ht = HashTable(size=1)
    ht.insert("apple", 5)
    ht.insert("banana", 10)
    
    expected_output = "0: [('apple', 5), ('banana', 10)]"
    assert str(ht) == expected_output
