## Export LTspice AC analysis data as  `.tsv` with Python in *NIX systems

For freeware, LTspice is a great circuit analysis tool. However, its data export features are lacking. You can export the waveform data as a `.txt` by right-clicking as shown below.

![](https://raw.githubusercontent.com/aryadee/LTspice-Data-Export/master/Images/LTspice.png)

For typical AC analysis, this outputs a `.txt` file with inconvenient formatting for the voltage if you want to import the data to another program.

```
Freq.	V(n002)
1.00000000000000e+000	(-5.39879373612431e+001dB,8.99884945816811e+001�)
1.25892541179417e+000	(-5.19879374626541e+001dB,8.99855155366172e+001�)
```

 You can write a script to enter the data in MATLAB,  Excel, etc., <u>but I've already done it for you</u> and saved you some time

```
Frequency (Hz)	Gain (dB)	Phase (°)
1.00000000000000	-53.9879373612431	89.9884945816811
1.25892541179417	-51.9879374626541	89.9855155366172
```

## How to use

**Just run the script in your terminal and drag and drop the LTspice data `.txt`. The `.tsv`	 file will be created at the original directory.** 

Optionally, you can output as a `.csv`  and/or scientific notation with the ` -c` and `-s` flags switches respectively.

You will need Python 3 or above and a GNU/Linux or macOS computer. If you're using windows, I think it's only the `    os.system('clear')` commands that are incompatible. You can just copy paste the rest as you need.

Now you can properly analyze the waveform or just make pretty charts for your documents.

![](https://raw.githubusercontent.com/aryadee/LTspice-Data-Export/master/Images/Report.png)

### Next features

-   [x] Add options for exporting as CSV and/or using scientific notation.
-   [ ] Handle other unit types, not just AC voltage and frequency

