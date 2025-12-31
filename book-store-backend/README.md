BookStore Backend

Миграции:  
``` 
// Создать файл миграции
alembic revision --autogenerate -m "Added user table"

// Выполнить миграции
alembic upgrade head
```
Для моделей использовать db.mixin.BaseModel или db.mixin.BaseModelUUID
