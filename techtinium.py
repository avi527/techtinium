'''
STEP 1 :- validation on hours and units capacity
STEP 2 :- create json structure as per requirments asign in machineunits,machineprice,fnloutput variables
STEP 3 :- use top to botton mathology for no. of machine count
STEP 4 :- calculate per unit cost with hours
STEP 5 :- all value put in fnloutput structure for desired output
STEP 6 :- finally print desired output

NOTE :- as per your output you had follow bottom to top methology but here i did use top to bottom methology
'''





machineunits={"Large":"10","XLarge":"20","2XLarge":"40","4XLarge":"80","8XLarge":"160","10XLarge":"320"}

machineprice={"Large":[{"newyork":"120", "india":"140","china":"110"}],
"XLarge":[{"newyork":"230", "india":"0","china":"200"}],"2XLarge":[{"newyork":"450", "india":"413","china":"0"}],
"4XLarge":[{"newyork":"774", "india":"890","china":"670"}],"8XLarge":[{"newyork":"1400", "india":"1300","china":"1180"}],
"10XLarge":[{"newyork":"2820", "india":"2970","china":"0"}]}


fnlOutput={"Output": [{"region": "","total_cost": "","machines": []},{"region": "","total_cost": "","machines": []},{"region": "","total_cost": "","machines": []}]}
hour=int(input("Enter Number Of Hours")) 
userInput=int(input("Enter Capacity Of Units")) 
if (hour !=0) and (userInput !=0):
	ilist={}
	check=0
	p=1
	q=userInput
	region=['newyork','india','china']
	getIndiaPrices={}
	getNewyorkPrices={}
	getChinaPrices={}
	indiaTotCost=0
	newyorkTotCost=0
	chinaTotCost=0
	#reverse mchine units(use top to botton methology )
	reverseMachineUnit={}
	for k,v in machineunits.items():
	    dict_element={k:v}
	    dict_element.update(reverseMachineUnit)
	    reverseMachineUnit=dict_element
	#print(reverseMachineUnit)

	#machine moveing round count 
	for k,v in reverseMachineUnit.items():
			p,q=divmod(q, int(v))
			ilist[k]=p
			#print(p,"*********",q,"***",check)

	#calculate per unit cost with hour		
	for keys,val in machineprice.items():
		getIndiaPrices[keys]=int(val[0]['india'])*hour
		getNewyorkPrices[keys]=int(val[0]['newyork'])*hour
		getChinaPrices[keys]=int(val[0]['china'])*hour

	#calculate cost with region
	for x,y in getIndiaPrices.items():
		for g,h in ilist.items():
			if x == g:
				indiaTotCost +=y*h
	for x,y in getNewyorkPrices.items():
		for g,h in ilist.items():
			if x == g:
				newyorkTotCost +=y*h
	for x,y in getChinaPrices.items():
		for g,h in ilist.items():
			if x == g:
				chinaTotCost +=y*h

	#machine list
	machinelist = list(ilist.items()) 
	#print(machinelist,'machinelist')


	#data append and insert in desired output structure
	fnlOutput['Output'][0]['region']=region[0]
	fnlOutput['Output'][0]['total_cost']= newyorkTotCost
	fnlOutput['Output'][0]['machines']= machinelist  
	fnlOutput['Output'][1]['region']=region[1]
	fnlOutput['Output'][1]['total_cost']= indiaTotCost
	fnlOutput['Output'][1]['machines']= machinelist  
	fnlOutput['Output'][2]['region']=region[2]
	fnlOutput['Output'][2]['total_cost']= chinaTotCost
	fnlOutput['Output'][2]['machines']= machinelist  
	print(fnlOutput)
else:
	print("please re-enter machine capacity and no of hours" )




	
		

