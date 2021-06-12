# Easter-Pascha-Date

## A project made for finding Easter's date with Gauss's Algorithm.

The symbolism : [x]<sub>n</sub> = (x mod n) is being used to denote the remainder of the devision x divided by n.  
Also the symbolism "Y" is being used to represent a year.

## Some definitions and explanations of the following terms have been provided

1. **Metonic Cycle**
2. **Golden Number of a year**

   golden_number(year) = [Y]<sub>19</sub> + 1  **or**  gn(Y) = [Y]<sub>19</sub> + 1
3. **Epact of a year**

    E[Y] = [11 · (gn(Y) - 1) + 8]<sub>30</sub>  **or**  E[Y] = [11 · gn(Y) - 3]<sub>30</sub>
4. **Pascha Full Moon date**

    2 + [19 · [Y ]<sub>19</sub> + 16]<sub>30</sub> of April

For a complete overview of the project you can read the pdf file with name [*Finding the date of Easter with Gauss’s Algorithm: An implementation in Python*](https://github.com/kostasthanos/Easter-Date/blob/master/Finding%20the%20date%20of%20Easter%20with%20Gauss%E2%80%99s%20Algorithm:%20An%20implementation%20in%20Python.pdf) in which the above definitions are being explained in detail. You are free to use this file, just leave a reference to it's url-link « https://github.com/kostasthanos/Easter-Pascha-Date/blob/master/Finding%20the%20date%20of%20Easter%20with%20Gauss%E2%80%99s%20Algorithm:%20An%20implementation%20in%20Python.pdf »
In addition, at the end of the work, both Orthodox and Catholic Easter dates for the years 2000 to 2100 are presented. Finally, the years where Orthodox and Catholic dates are coincided are highlighted. Below you can see a part from the results for the years 2000 to 2055.

<p align="center">
  <img width="500" height="500" src="easter_dates.png">
</p>

Αll the mathematical calculations and algorithms presented in this work have also been implemented in Python for a better picture of the results. Python file : *[easter_date.py](https://github.com/kostasthanos/Easter-Date/blob/master/easter_date.py)*.

##  Author
* **Konstantinos Thanos**
