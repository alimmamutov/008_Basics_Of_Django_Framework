# Мамутов Алим - Интернет магазин мебели
***
****Служебное****
***
*Для установки нужного venv:*
    
    pip install -r requirements.txt     
(requirements.txt лежит в корне проекта)

*Для выгрузки venv:*

    pip freeze > requirements.txt
***
***

**Урок 02**

_****Внимание: Версия Django == 2.2****_

1. Реализовать наследование шаблонов в проекте. Меню подключить как подшаблон.


    Сделал это на всех страницах

2. Реализовать в проекте механизмы работы со статическими файлами и URL-адресами, которые прошли на уроке.


    Реализовал для подключения css в base.html


3. Поработать с шаблонными тегами и фильтрами (заглавные буквы, вывод текущей даты в шаблоне).


    Заглавные буквы заголовка реализованы в базовом шаблоне, Текущая дата реализована на страницt product.html


4. Организовать вывод динамического контента на страницах (элементы меню, список товара, заголовок страницы).


    Реализовано в inc_products_categories_area_content.html, который встраивается в index.html, являющийся наследником  base.html

5. *Организовать загрузку динамического контента в контроллеры с жесткого диска (например, в формате «json»).


    Реализовано в views.py для реквеста домашней страницы (в контекст передается список товаров, выводимых при открытии домашней страницы)

**Урок 03**

1. Настроить проект для работы с медиафайлами.


    Настроил settings.py.
    Настроил глобальный urls.py для адресации media 
    В корне проекта создал директорию /media/


2. Создать модели в проекте (обязательно должно быть поле с изображениями) и выполнить миграции.


    Создал классы для Product и ProductCategory в models.py
    Связал две таблицы связью один ко многим
    Создал миграции и выполнил их

3. Поработать с моделями в консоли.


    Научился создавать, выводить и удалять экземпляры класса

4. Создать суперпользователя. Настроить админку и поработать в ней.


    Создал суперпользователя LOGIN:Django PASSWORD:geekbrains

5. Организовать работу с моделями в контроллерах и шаблонах.


    Изменил Контроллер index(request) в views.py
    Организовал заполнение шаблона index из модели

6. Реализовать автоматическое формирование меню категорий по данным из модели.


    Реализовал через инключзирование подшаблона inc_catagories_menu
    Не смог реализовать установку активного класса хотя бы на первый элемент


7. *Создать диспетчер URL в приложении. Скорректировать динамические URL-адреса в шаблонах. Поработать с имитацией переходов по категориям в адресной строке браузера.


    Добавил urls.py в папку mainapp, сослался на него в глобальном urls.py, назначив пространство имен "main"
    Сформировал присваивание id товара к концу ссылки на товар, теперь при нажатии на ссылку товара на главной странице, открывается product details определенного товара

8. *Организовать загрузку данных в базу из файла.


    Реализовал через импорт библиотеки import/export.
    Прописал его поведение в admin.py


**Урок 04**

1. Создать модель пользователя в проекте. Обязательно добавить поле с изображением и возрастом. 
   Выполнить настройки в файле конфигурации.
   
    
    Создал приложение authapp, добавил модель ShopUser. Настроил диспетчер юрл и контроллер, 
    создал форму и шаблоны
    Прописал AUTH_USER_MODEL = 'authapp.ShopUser' в settings.py - Теперь по дефолту модель 
    для пользователей Django ShopUser, а не стандартный User

2. Организовать загрузку данных в БД из файла.
   
    
    Создал fill_db в mainapp/management/commands.py
    Сформировал json файлы для категорий и продуктов

3. Реализовать механизм аутентификации в проекте.
   

      Реализовано в приложении authapp

4. Реализовать механизм регистрации пользователя.
      
      
      Реализовано в приложении authapp

5. Организовать просмотр и редактирование данных пользователем.
   

      Реализовано в приложении authapp

6. *Разобраться с механизмом валидации данных формы. Создать свои валидаторы.


      Узнал, что валидация прописывается на стадии прописывания модели
      В аргумент validators передается массив функций валидыции
      Можно использовать готовые валидаторы из пакета джанго django.core.validators (использовал в моделях mainapp)
      Можно прописывать свои кастомные валидаторы, вызывая в них ошибку ValidationError из пакета django.core.exceptions (использовал в модели authapp)


####*ps:*
*для установки правильного venv воспользуйтесь requirements.txt (requirements.txt лежит в корне проекта)*