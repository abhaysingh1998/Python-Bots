## ABOUT:-

* A Simple echo bot works with facebook API . Just type in your message and it will echo the same message back to you .

## INITIATION :-

* Firstly goto [facebook developers page](https://developers.facebook.com) and signup there . Just click on `create an app` . Provide appname and category there and ur app will be made with no ease. Now just provide it your fb page details (if u don't have create one) . Now get the `token` from there .

## INTERMEDIATE :-

* Run `pip install -r requirements.txt` command to install the required modules . Now run `python app.py`  
* This will coax it to run on your localhost that means offline . Now if u want it to be online install `ngrok` . Start ngrok by executing the command ```ngrok http 80``` . Ngrok will Create a tunnel to the localhost and makes ur app to run on a live public IP adress ;)  !!
* Then give the ngrok server url to webhooks at developers.facebooks.com page . Done XD . Now open your bot in your fb page and type a meassage . You will definitely be able to see it in your terminal . Make sure app is already running ( ```python app.py```) on localhost before doing all this stuff .

## Deployment :-

* If u want to deploy your app then `Heroku` is best to accomplish it. just install heroku cli to your machine . After deploying it there (read more about deploying an app to heroku) you have to change your previous webhook at developers page . Just put your heroku app url there . 


Your `Echo_Bot` is Ready :)  




