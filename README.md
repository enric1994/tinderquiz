![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fgithub.com%2Fenric1994%2Ftinderquiz)

During 2 months I used this Tinder bot that provided me **63 Whatsapp contacts** of random girls. 

Basically, the bot is a **gamechat** where the girls have to answer 9 questions correctly in order to get my phone number 😎

My system perform two operations:
* Hit random likes (200 per day)
* Answer questions to my matches


## Example

Here's my profile photo (I focused on catalan girls, so all the texts are in Catalan):

<p align="center">
 <img src="images/Screenshot_20170710-141118.png" width="350">
</p>

Basically, I present myself and explain the challenge.

Then, when the bot match with a girl, it send the first answer: **Wich is the capital of Sweden?**

And when the bot detects the correct answer (Estocolm in Catalan) it sends the next question:

  <div align="center">
   <img src="images/Screenshot_20170710-141129.png" width="350">
   <img src="images/Screenshot_20170710-141136.png" width="350">
  </div>


<p align="center">
</p>

And so on...

<div> 
  <div>
     <img src="images/Screenshot_20170710-141144.png" width="300">
     <img src="images/Screenshot_20170710-141148.png" width="300">
  </div>
   <div>
     <img src="images/Screenshot_20170710-141159.png" width="300">
     <img src="images/Screenshot_20170710-141204.png" width="300">
  </div>
  <div>
     <img src="images/Screenshot_20170710-141210.png" width="300">
     <img src="images/Screenshot_20170710-141216.png" width="300">
  </div> 
</div>

Wow! Finally the target complete all the questions! Now he is awarded wit my phone number, I hope that he chat me on Whatsapp... 😆

___

### Integration with Telegram

I used Telegram bot that inform me of the new girls that complete the quiz:

<p align="center">
 <img src="images/photo_2018-05-21_23-14-29.jpg" width="250">
</p>

### Infrastructure
* In order to communicate with the Tinder API I used [this](https://github.com/charliewolf/pynder) Python wrapper.
* The full system was deployed at AWS (Amazon Web Services) under a free tier machine.




