### Замер производительности скользящей средней 
Для сравнения реализаций SMA через список и через `deque` используйте флаг `-
benchmark`: 
```bash 
python main.py --kind random --n 5000 --window 20 --benchmark 