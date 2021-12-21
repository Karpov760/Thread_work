1.Написать программу трёхленточной сортировки линейного списка, распараллелив процессы разбора и слияния списков. Количество потоков и способы их синхронизации определить самостоятельно.	
2.Смоделировать механизм рандеву для решения задачи нахождения значения функции ex по ее разложению в ряд Маклорена. В качестве вызывающей задачи взять функцию нахождения суммы элементов ряда, а в качестве обслуживающих задач – функцию нахождения факториала и функцию нахождения степени аргумента.
Примечание: найдите, что такое “механизм рандеву”.

3.Даны n файлов, содержащие неубывающие последовательности чисел. Написать программу, выполняющую слияние этих файлов в один таким образом, чтобы выборку данных из файлов и формирование результирующего файла выполняли три разных потока. Каждый из потоков выборки данных может прочитать очередное значение из своего файла только тогда, когда поток формирования результата передал соответствующее число в файл. Поток формирования результата может выполнять обработку данных только тогда, когда оба потока выборки предоставили ему данные.
