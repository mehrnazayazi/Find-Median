# Find-Median
This projects finds the median of the array made by merging two given sorted arrays
##The main idea
When compaing the median of two arrays there will be two cases
if med_1 == med_2 
then in the median of the final array would be the same(the left sides of medians will merge together and the right sides together)
in case the two medians are not equal:
Assume that the length of the first array(m) > length of the second array(n)
then we can eliminate n numbers from our calculations. (n/2 from the first array and n/2 from the second)
That is because in any case at least half of one array is going to be on the left side of the final median and half of the other array would be on the right side of the median. 
We could eliminate (n+m/2) of the cells but eliminating the same number of cells from each side of the final array leaves us with a smaller version of the same problem and thus recursion.
