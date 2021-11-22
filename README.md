# Мамутов Алим - Интернет магазин мебели

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