# Python Excel Template Code
A python template code that can save unicode data in xls file with headers included
### Requirements
<pre>pip3 install xlutils</pre>
### Use Cases
Tired of storing unicode data in csv file but can't see that data in excel viewer or your format of data is changed by excel viewer? xlutils is a best choice to write unicode characters easily and write in any dynamic cell location you want. I wrote the code so that it can save row-wise based on given data and function call. All you have to do is, install the module using above command mentioned in the requirements. and then call the function saveData() with first parameter set as data list and second parameter being the file name without extension.
### Module limitation
xlutils cannot save xlsx format of data. So you always have to save file name as .xls (predefined already in the function body).
