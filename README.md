# Life-Insurance-with-Annuity
This is a pricing program for a whole-life life insurance with annuity

This is a pricing program for a life insurance with premium payment peiord of 20 years and the following benefits
1. Death/ Total disability benefit:
   - during the premium payment peroid (<=the 20th policy year):</br> 
     max(policy value, 1.06 times total premium paid, 3 times of amount insured)</br> 
   - after the premium payment period (>=the 21st policy year):</br> 
     max(policy value, 1.06 times total premium paid, 1 time of amount insured)</br> 
2. Life annuity:</br> 
   - payable annually 
   - during the premium payment peroid (<=the 20th policy year):</br> 
     5% of the premium</br> 
   - after the premium payment period (>=the 21st policy year):</br>
     50% of the premium</br> 
3. Endowment:</br> 
   When the policy holder reaches age 105, the endowment is paid as 1.06 times the total premium paid

The motality rate was based on the Taiwan Life Table fifth edition and proveided as a csv file in the following 

