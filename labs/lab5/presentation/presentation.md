---
## Front matter
lang: ru-RU
title:  Основы информационной безопасности. Лабораторная работа № 5
subtitle: Дискреционное разграничение прав в Linux. Исследование влияния дополнительных атрибутов
author: |
	Сунгурова Мариян М.
institute: Российский Университет дружбы народов
date: 05.10.2024

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
slide_level: 2
aspectratio: 169
section-titles: true
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
---

# Информация

## Докладчик

:::::::::::::: {.columns align=center}
::: {.column width="70%"}

  * Сунгурова Мариян М.
  * студентка группы НКНбд-01-21
  * Российский университет дружбы народов
 
:::
::: {.column width="30%"}



:::
::::::::::::::

# Вводная часть

## Цель работы

Целью данной лабораторной работы является изучение механизмов изменения идентификаторов, применения SetUID- и Sticky-битов, а также получение практических навыков работы в консоли с дополнительными атрибутами и рассмотрение работы механизма смены идентификатора процессов пользователей, и влияние бита Sticky на запись и удаление файлов.

## Теоретические сведения

При работе с командой chmod важно понимать основные права доступа, которые назначают файлам или каталогам. В Linux используется три основных типа прав доступа:

  - Чтение (Read) — обозначается буквой «r». Предоставляет возможность просматривать содержимое файла или каталога.
  - Запись (Write) — обозначается буквой «w». Позволяет создавать, изменять и удалять файлы внутри каталога, а также изменять содержимое файла.
  - Выполнение (Execute) — обозначается буквой «x». Дает разрешение на выполнение файла или на вход в каталог.

## Теоретические сведения

Каждый из указанных выше типов прав доступа может быть назначен трем группам пользователей:

  - Владелец (Owner) — пользователь, который является владельцем файла или каталога.
  - Группа (Group) — группа пользователей, к которой принадлежит файл или каталог.
  - Остальные пользователи (Others) — все остальные пользователи системы.

Комбинация этих базовых прав доступа для каждой из групп пользователей определяет полный набор прав доступа для файла или каталога.

# Выполнение лабораторной работы

## Выполнение лабораторной работы

Проверим установлен ли компилятор gcc, а также отключим SELinux(рис. @fig:001)

![Подготовка лабораторного стенда](image/1.JPG){#fig:001 width=60%}

## Выполнение лабораторной работы

![Подготовка лабораторного стенда](image/2.JPG){#fig:021 width=70%}

## Выполнение лабораторной работы

Войдем в систему от имени пользователя guest и создадим программу simpleid.c, которая выводит идентификатор пользователя и группы(рис. @fig:002)

![Текст программы simpleid.c](image/3.JPG){#fig:002 width=60%}

## Выполнение лабораторной работы

Теперь скомпириуем программу с помощью gcc, затем, запустив её, увидим, что она выводит идентификаторы пользователя и группы 1001 и 1001 для guest, что совпадает с выводом команды id(рис. @fig:003)

![Запуск программы simpleid](image/4.JPG){#fig:003 width=60%}

## Выполнение лабораторной работы

Усложним программу, добавив вывод действительных идентификаторов(рис. @fig:004).

![Текст программы simpleid2.c](image/5.JPG){#fig:004 width=60%}

## Выполнение лабораторной работы

Теперь скомпириуем программу с помощью gcc, затем, запустив её, увидим, что она выводит идентификаторы пользователя и группы 1001 и 1001 для guest, что совпадает с выводом команды id(рис. @fig:005).

![Запуск программы simpleid2](image/6.JPG){#fig:005 width=60%}

## Выполнение лабораторной работы

От имени суперпользователя изменим владельца файла /home/guest/simpleid2 и установим SetUID-бит. Проверим корректность установленных прав и опять запустим simpleid2(рис. @fig:006).

![Изменение владельца и запуск программы simpleid2 с установленным SetUID-битом](image/7.JPG){#fig:006 width=60%}

## Выполнение лабораторной работы

Проделаем аналогичные действия относительно SetGID-бита(рис. @fig:007):

![Запуск программы simpleid2 с установленным SetGID-битом](image/8.JPG){#fig:007 width=60%}

## Выполнение лабораторной работы

Создадим программу для чтения файлов readfile.c(рис. @fig:008):

![Текст программы readfile.c](image/9.JPG){#fig:008 width=60%}

## Выполнение лабораторной работы

Скомпилируем её и сменим владельца у файла с текстом программы, затем изменим права так, чтобы только суперпользователь (root) мог прочитать его, и проверим корректность настроек(рис. @fig:008):

## Выполнение лабораторной работы

Сменим у программы readfile владельца и установим SetUID-бит. Теперь эта программа может прочитать файл readfile.c даже с пользователя guest, также она может прочитать файл /etc/shadow, владельцем которого guest также не является, так как программа readfile теперь имеет все права пользователя root(рис. @fig:010):

![Установка SetUID-бита на исполняемый файл readfile и проверка прав](image/10.JPG){#fig:010 width=60%}

## Выполнение лабораторной работы

Проверим, что установлен атрибут Sticky на директории /tmp(в конце стоит t). Затем от имени пользователя guest создадим файл file01.txt в директории /tmp со словом test, затем просмотрим атрибуты у только что созданного файла и разрешим чтение и запись для категории пользователей «все остальные». После этого от пользователя guest2 попробуем дозаписать в этот файл новое слово, однако получим отказ, также нам отказано в перезаписи и удалении этого файла. Если же убрать Sticky бит, то нам будет разрешено удаление этого файла(рис. @fig:011)

## Выполнение лабораторной работы

![Подключение образа диска дополнений](image/11.JPG){#fig:011 width=70%}

# Выводы

## Выводы

В результате выполнения данной лабораторной работы работы были рассмотрены:

- Механизмы изменения идентификаторов, применения SetUID- и Sticky-битов.
- Получение практических навыков работы в консоли с дополнительными атрибутами.
- Механизм смены идентификатора процессов пользователей, а также влияние бита Sticky на запись и удаление файлов.
