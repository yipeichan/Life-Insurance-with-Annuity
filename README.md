# Life-Insurance-with-Annuity
<a href="https://yipeichan.github.io"><b>Link to additional explanations</b></a>
<br>
## Introduction
This program was modified from one of the insurance products that I devised. It launched the market on November 30th 2017, and had a pretty good sales record. The insurance contract has a premium paying term of 20 years and provides benefits as follows, </br> 
</br> 
<b>1. Death/ Total disability benefit:</b><br>
   - during the premium paying term (<=the 20th policy year):<br> 
     max(policy value, 1.06 times total premium paid, 3 times of amount insured)<br> 
   - after the premium paying term (>=the 21st policy year):<br> 
     max(policy value, 1.06 times total premium paid, 1 time of amount insured)</br> 

<b>2. Life annuity:</b></br> 
   - payable annually <br>
   - during the premium paying term ( before the 20th policy year):<br> 
     5% of the premium<br> 
   - after the premium paying term ( after the 20th policy year):<br>
     50% of the premium 

<b>3. Endowment:</b><br> 
      When the policy holder reaches age 105, the endowment is paid as 1.06 times the total premium paid<br>

The mortality rate was based on the Fifth Life Experience Table of Taiwan Life Insurance Industry and provided as a csv file in the following <br>

<br>

## An Insurance Policy Catered to Human Life Cycle
<div class="f">
The main target client group of this contract are people aged between 20 to 55. People in such age range are often those who bring home the backon; they go out to work, on business trevels frequently, which exposed them to higher risks on streets or abroad. Once accidents strike, he/she may lose the ability to work, affecting financial situation of entire family. Therefore during the premium paying term, which is 20 years, the policy provides high leverage of death coverage compared to the amount of premium paid. After 20 years, it would be the time of retirment, and the policy provides 50% of the annual premium until the insured reaches age 105. The annuity helps policy beneficiaries prevent money shortage in face of prolonged life expectancy.<br><br></div>

![financial-plan](https://user-images.githubusercontent.com/24948460/49664603-4e8d0e80-fa8d-11e8-8305-201c7a5ae0c7.png)<font size="xx-small">(photo from omtatsat.tk)</font>

<br>

## Pricing Algorithm
n: premium paying term<br> 
i: assumed interest rate<br> 
x: age insured<br> 
<br>
<b>1. Death/ Total Disability Benefit</b> <br>
<img width="552" alt="screen shot 2018-12-07 at 11 31 20 pm" src="https://user-images.githubusercontent.com/24948460/49656446-55f5ed00-fa78-11e8-8ae4-f6b02ad98857.png">
<br>

<b>2. Annuity</b><br>
<img width="429" alt="screen shot 2018-12-07 at 11 31 43 pm" src="https://user-images.githubusercontent.com/24948460/49656445-55f5ed00-fa78-11e8-96e5-687063f8050c.png">

<br>

<b>3. Endowment</b><br>
<img width="354" alt="screen shot 2018-12-07 at 11 31 50 pm" src="https://user-images.githubusercontent.com/24948460/49656444-55f5ed00-fa78-11e8-8ec8-454c25a00715.png">

<b>4. Insurance Premium</b> <br>
<img width="322" alt="screen shot 2018-12-07 at 11 31 55 pm" src="https://user-images.githubusercontent.com/24948460/49656443-555d5680-fa78-11e8-9f5f-dcc66b8bdbe3.png">
<br>

## Pricing Program Applications
<div class="f">
The program starts with asking you to enter information about the age, loading and the sex you want to test. The loading is the markup of net premium, which is one source of the profits that insurance companies earn, and most of the time the source of agent commissions. After entering the information you want to know, the program would demonstrate the asymptotic process and generate the result if the premium converges under the conditions you entered. 
<br>
For example, to price the insured who is
<br>
1. male, aged 35, and the loading set to be 10% <br>
<img width="945" alt="screen shot 2018-12-08 at 12 08 48 am" src="https://user-images.githubusercontent.com/24948460/49659079-61e4ad80-fa7e-11e8-8da2-9278f7d3bf67.png">
<br>
<br>
2. female, aged 62, and the loading set to be 9.3%<br>
<img width="675" alt="screen shot 2018-12-16 at 8 24 43 pm" src="https://user-images.githubusercontent.com/24948460/50053470-c4ba0100-0170-11e9-9ace-9bebf310c363.png">

</div>
