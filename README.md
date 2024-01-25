# TurboGaser

Программа, позволяющая проводить расчет газотурбинных двигателей. Написана для расчета курсовых и дипломных  проектов на кафедре "Газотурбинные двигатели и комбинированные установки" (Э3) МГТУ им. Н.Э. Баумана.

## Управление проектами
Все необходимые для расчета данные находятся в проектах. Управление проектами происходит черех команду `project`.

Для отслеживания всех существующих проектов в домашней директории создается файл `.turbo_gaser_config`, в котором записывается текущий проект, а также список существующих проектов. Поэтому, чтобы не нарушать консистентность данных, **не рекомендуется вручную переименовывать и перемещать проекты**. Делать это нужно только с помощью соответствующих подкоманд.

### Создание нового проекта
Чтобы создать новый проект с названием `project_name`, который располагается в директории `PROJECT_DIR`, воспользуйтесь командой:

```bash
turbogaser new [-p PROJECT_DIR] project_name
```

По умолчанию, если не указывать директорию, проект создается в текущей директории.

### Удаление проекта
Чтобы удалить существующий проект, воспользуйтесь следующей командой:

```bash
turbogaser delete project_name
```

### Просмотр списка существующих проектов
Чтобы просмотреть список существующих проектов, воспользуйтесь следующей командой:

```bash
turbogaser list
```

### Изменить текущий проект
Чтобы изменить текущий проект, воспользуйтесь следующей командой:

```bash
turbogaser set_current project_name
```

### Изменить текущий проект
Чтобы изменить текущий проект, воспользуйтесь следующей командой:

```bash
turbogaser set_current project_name
```

### Узнать текуйщи проект
Чтобы получить название текущего проекта, воспользуйтесь следующей командой:

```bash
turbogaser get_current
```

*Информация дополняется по ходу написания программы*
