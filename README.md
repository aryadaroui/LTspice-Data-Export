## Export LTspice Data as TSV with Python

For freeware, LTspice is a great circuit analysis tool. However, its data export features are lacking. You can export the waveform data as a .txt by right-clicking as shown below.

![](https://raw.githubusercontent.com/aryadee/LTspice-Data-Export/master/Images/LTspice.png)

This outputs .txt file with inconvenient formatting. You can write a script to enter the data in MATLAB,  Excel, etc., but I've already done it for you. 

## How to use

Just run the script in your terminal and drag and drop the LTspice data `.txt` and the .tsv file will be created at its directory.

Now you can properly analyze the waveform or just make pretty charts for your documents.

![](https://raw.githubusercontent.com/aryadee/LTspice-Data-Export/master/Images/Report.png)



### TODO

Add options for exporting as CSV and/or using scientific notation.
