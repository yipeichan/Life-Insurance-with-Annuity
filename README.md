# Life-Insurance-with-Annuity

## Introduction
This is a pricing program for a life insurance with premium payment peiord of 20 years and the following benefits:</br> 
<b>1. Death/ Total disability benefit:</b><br>
   - during the premium payment peroid (<=the 20th policy year):<br> 
     max(policy value, 1.06 times total premium paid, 3 times of amount insured)<br> 
   - after the premium payment period (>=the 21st policy year):<br> 
     max(policy value, 1.06 times total premium paid, 1 time of amount insured)</br> 

<b>2. Life annuity:</b></br> 
   - payable annually <br>
   - during the premium payment peroid ( before the 20th policy year):<br> 
     5% of the premium<br> 
   - after the premium payment period ( after the 20th policy year):<br>
     50% of the premium 

<b>3. Endowment:</b><br> 
      When the policy holder reaches age 105, the endowment is paid as 1.06 times the total premium paid<br>

The motality rate was based on the Fifth Life Experience Table of Taiwan Life Insurance Industry and proveided as a csv file in the following <br>

## Pricing Algorithm
n: premium payment period <br>
<br>
<b>1. Death/ Total Disability Benefit</b> <br>
<img width="322" alt="screen shot 2018-12-07 at 11 31 55 pm" src="https://user-images.githubusercontent.com/24948460/49656443-555d5680-fa78-11e8-9f5f-dcc66b8bdbe3.png">
<br>

<b>2. Annuity</b><br>
<img width="354" alt="screen shot 2018-12-07 at 11 31 50 pm" src="https://user-images.githubusercontent.com/24948460/49656444-55f5ed00-fa78-11e8-8ec8-454c25a00715.png">

<br>

<b>3. Endowment</b><br>
<img width="429" alt="screen shot 2018-12-07 at 11 31 43 pm" src="https://user-images.githubusercontent.com/24948460/49656445-55f5ed00-fa78-11e8-96e5-687063f8050c.png">

<b>4. Insurance Premium</b> <br>
<img width="552" alt="screen shot 2018-12-07 at 11 31 20 pm" src="https://user-images.githubusercontent.com/24948460/49656446-55f5ed00-fa78-11e8-8ae4-f6b02ad98857.png">
<br>

## Pricing Program Applications

