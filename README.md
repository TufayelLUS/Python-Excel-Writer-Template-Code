# Python Excel Writer Template Code
A python template code that can save unicode data in xls/xlsx file with headers included
# Performance Info
Do not use the template_xls.py or template_xlsx.py in case you are planning to store a large number of rows in your excel file as the codes will be gradually slower based on the number of rows you have in an existing excel file.<br>
You are highly recommended to use the template_xls_fast.py or template_xlsx_fast.py version by utilizing the list of rows stored in your program memory and then writing them into excel file all at once with this code. It's a faster approach for these templates to work perfectly.
### Requirements
For the xls version script:
<pre>pip3 install xlutils</pre> 
For the xlsx version script:
<pre>pip3 install openpyxl</pre>
### Use Cases
Tired of storing unicode data in csv file but can't see that data in excel viewer or your format of data is changed by excel viewer? xlutils/openpyxl is a best choice to write unicode characters easily and write in any dynamic cell location you want. I wrote the code so that it can save row-wise based on given data and function call. All you have to do is, install the module using above command mentioned in the requirements. and then call the function saveData() with first parameter set as data list/row list(depending on the template version) and second parameter being the file name without extension.
