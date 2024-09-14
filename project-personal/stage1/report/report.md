---
## Front matter
title: "Основы информационной безопасности"
subtitle: "Индивидуальный проект. Этап № 1. Установка Kali Linux"
author: "Сунгурова Мариян М."

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: false # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Постановка задачи

Целью данной работы является установка дистрибутива Kali Linux в виртуальную машину.

# Выполнение лабораторной работы

Скачаемаем образ Kali Linux[@kali:bash]. Создадим виртуальную машину. 

![Создание новой ВМ](image/img_1.JPG){#fig:001 width=70%}

Добавим новый привод оптических дисков и выберите образ операционной системы, укажем имя виртуальной машины, тип операционной системы -- Linux, Debian (64-bit), рамзер основной памяти  -- 2048 МБ,  конфигурацию жёсткого диска — загрузочный, VDI (BirtualBox Disk Image), динамический виртуальный диск,  размер диска — 40 ГБ (или больше)(рис. @fig:002 ).

![Создание новой виртуальной ОС](image/img_2.JPG){#fig:002 width=70%}



Установим имя хоста, пользователя и пароль суперпользователя(рис. @fig:003 - @fig:005):

![Установка имени хоста](image/img_4.JPG){#fig:003 width=70%}

![Установка имени пользователя](image/img_5.JPG){#fig:004 width=70%}

![Установка пароля для root](image/img_6.JPG){#fig:005 width=70%}

Установим пароль для root и пользователя с правами администратора.

![Выбор типа разделения диска](image/img_7.JPG){#fig:006 width=70%}

![Информация о разделении диска](image/img_8.JPG){#fig:007 width=70%}

Выберем базовое ПО для начальной установки(рис. @fig:008):

![Выбор пакетов ПО](image/img_9.JPG){#fig:008 width=70%}

Вход в аккаунт(рис. @fig:009, @fig:010):

![Вход в систему](image/img_10.JPG){#fig:009 width=70%}

![Рабочий стол](image/img_11.JPG){#fig:010 width=70%}

# Выводы

В результате выполнения работы был уавстановлен дистрибутив Kali Linux в виртуальную машину.

# Список литературы{.unnumbered}

::: {#refs}
:::