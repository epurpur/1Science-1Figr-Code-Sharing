# 1Science-1Figr-Code-Sharing


GitHub repository for 1Figr data


Steps to use data...

1- Save the 'JournalsPerProvider' tab from your master copy of the 1Figr/1Science Dataset as CSV file as 'JournalsPerProvider.csv'.  Must be in 
UTF-8 encoding to be read correctly by Pandas. I suggest you do this by copy and pasting all contents of the 'JournalsPerProvider' tab into a new workbook in excel and saving that as 'JournalsPerProvider.csv'.

2- Notice in the 'JournalsPerProvider' CSV document that the column headers begin on row 8. Keep it this way. The code 
skips to the 8th row, and then begins parsing the data.

*Probably the easiest way to do steps 3-8 is in Microsoft Excel. 

3- Open the CSV document (JournalsPerProvider.csv) in excel and 
format the data in the following columns as 'general' data type with no decimal places. Do this by selected all the data in 
the column under the column header, right click, and 'format data'. If you don't do this, Pandas reads these as strings or 
some other undefined data type:
'Downloads JR1 2017', 'Downloads JR5 2017 in 2017', 'References', 'Papers' (These should be columns H,I,K,M in your dataset).

4- Rename the following columns under 'Papers per journal/provider by your institution's authors (As Measured in Scopus)' 
(should be columns AA - AJ) as 'papers_2008', 'papers_2009', 'papers_2010' and so on. Then change the data in all these 
columns to 'general' data type with no decimal places.

5- Repeat the process for all columns under 'References to journal/provider by your institution's authors (As measures in 
Scopus)' (should be columnns AK-AT) as 'ref_2008', 'ref_2009', 'ref_2010' and so on. Change data in these columns to 
'general' data type with no decimal places.

6- Repeat the process for all columns under 'OA papers in 1findr per journal/provider (Intersection with Scopus)' (should be 
columns AU-BC) as 'oa_papers_2008', 'oa_papers_2009', 'oa_papers_2010' and so on. Change data in these columns to 'general' 
data type with no decimal places.

7- Repeat the process for all columns under '% of OA papers in 1findr per journal/provider (intersection with Scopus)' (should 
be columns BD-BM) as 'oa_2008', 'oa_2009', 'oa_2010', and so on. Change the data in these columns to 'general' data type with 
no decimal places.

8- Repeat the process for all columns under 'Total Papers in Scopus per journal/provider' (should be columns BO-BX) as 
'total_2008', 'total_2009', 'total_2010', and so on. Change data in these columns to 'general' data type with no decimal 
places. 

*Lastly, keep in mind your 'JournalsPerProvider.csv' file should be saved in the working directory or same directory as the 
code. Otherwise you'll have to change the file paths at the beginning of each function to read to the new working directory. 


Now that you've formatted the data correctly, you should be able to "plug and play" all existing functions.
