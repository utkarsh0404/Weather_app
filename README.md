Firstly i ask the user input to the customer which is a city name.
after that i get the API details like "base_url" and "api_key" from the "open weather map".
Then I created a dictionary to add the required api parameters/ inputs link city name , appid and the unit of temperature i.e celcius and we get all this required parameters from the open weather map api itself .
then I make a api call request by simply adding library called request and as i want to get the data so i used function named "get" and in this function get i passed the "base_url" and the "A" Variable as it includes all the required details as mentioned above.
now i created a variable called "Data" to store the response.
Now to get only desired data from the API I created 3 variables called D ,H,T which contains information like Weather Description , Humidity and temperature respectively .
and lastly i just call the print to get the output .
