## Benchmark

Our algorithm is validated against 1000 records and the results are presented as tables below. Close to 88% of records don't possess any signature matching with our identifier and  12% records possess one matching our filtering identifier. 124 records possess 135 identifier occurrences, where 3 records contain 2 identifier occurrences in one record, 2 records with 3 identifier occurrences in one record and 1 record with 5 identifier occurrences in one record.

![benchmarkresults](/img/BMresults.png)


`Note:`

* (2)(3)(5) denotes 2, 3 and 5 signatures respectively in one record.

True and False prediction are evaluation results, where **True prediction** defines when algorithm results match with actual details correctly and **False prediction** defines when algorithm predicted wrongly from actual details.

Dont know class prediction is also considered as True prediction.

Algorithm Benchmark:

In 135 suspected occurrence algorithm produced 100% true results at end of two levels.  At first level which confirms on 60% of right results and those failed at first validation is sent for level 2 of validation and  predicted rightly by algorithm.