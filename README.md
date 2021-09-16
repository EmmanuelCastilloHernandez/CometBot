# Comet
## Open Source Discord.py bot to goof with
![Comet Logo](static/photoToRender/CometProfile.jpg)

Created by Emmanuel Castillo and in collaboration with Garen Gevorgyan. Current version is 2.0.0 `Aldebaran`

To see if the bot is up, check: https://cometbot.emmanuelch.repl.co

# What It Does
> It's a python bot ofc

###### Emmanuel Castillo

The Comet bot provides basic Discord Bot functionality, like a warning system and other commands to goof around with. This is all done using the __**[PyCord](https://github.com/Pycord-Development/pycord)**__ library.

It's modular and runs 24/7 thanks to __***Flask***__ and __***Uptime Robot***__

The website is coded in HTML and CSS working together. The animations are made possible because of [animistia](https://animista.net/play).

# Features
> Comet gives other bots like Sniped! a run for its money due to how it does thinngs differently

###### Emmanuel Castillo, *again*
As is, the bot is packed with features, such as:
* Snipes
> * Super Snipe
> * Image and GIF Snipes
> * Edit Snipe
* Text-to-Speech
* Revive functionality
> * #topic
> * AI Chatbot
* Blacklist
* Warning System
* Economy Game

### Snipes

#### Super Snipe
Typical snipe bots only snipe one message at a time and when another message gets deleted, so does that message. This bot solves that issue because it can capture up to five deleted messages before discarding them in favor of new ones.

To use it, use the command `#SuperSnipe` or `#ssnipe`, which will default to the first deleted message. For other messages, use `#SuperSnipe (number)` or `#ssnipe (number)` to see them. To make the experience more interesting, the command's buttons generate in a random pattern of colors

#### Image and GIF Snipe
Comet's regular snipe (`#snipe`) has the ability to snipe most GIF links and turn them into embedded images in order to preview a sniped GIF link in case you want to copy it.

Comet also allows for people to snipe deleted images, which don't ever get saved locally to the bot's Repl storage because the Comet Dev Team believes in Privacy and Transparency.

#### Edit Snipe
A message's meaning can be altered by obviously editing it. This means that if you wanted to see what the message read previously, you had to be there or download 3rd-Party addons to see it. Thankfully, Comet bypasses this by the creation of the `#edit` command, which shows you how a message was before it was edited and how it is after its edited. Multiple edit message viewing is planned for V3 by latest. Beware `#edit` has a 60-second timer to check what were the contents of the message before the command gets cleared.

### Text-To-Speech
Bots like Yggdrasil offer a TTS functionality, but its capped at 45 characters or even less if you dont pay for added-functionality. Comet introduces a 1200 character TTS that not only can it be as long as the person inputs, but also supports multiple languages thanks to gTTS. In addition, the command will translate the text to the language of your choice so Comet can dictate it in that language. To use TTS you do `#tts <text>` and then an embed will appear allowing you to choose your language. Suported languages are English, Spanish, Armenian, Korean, and Tagalog (Filipino)

### Revive Functionality
#### #topic
Servers die. This is due to a lack of new conversations that keep people engaged in the server. Thankfully, Comet tries to fix this by giving a random question using the `#topic` command, which will give a random question (or weird statement) to start a conversation.
#### AI Chatbot
The bot has a built-in Chat Bot due to CodeWithSwastik's and others' work on the PRSAW python library. To talk to the bot use the `:` prefix before the sentence you want to tell it. Note that this feature may be disabled at times because of the instability of PRSAW.

### Comet**CRISIS**
###### NOTE: This feature is recommended to be used **`only`** by people living in the United States, specifically the residents of Los Angeles County, California, U.S.A. and its neighbouring counties due to the limited resources Comet and its development/mantainance has. However, Comet still provides information for hotlines outside the US.
Life can be something incredibly beautiful, but also something that can become challeging for one's mind and body. For those whose struggles are becoming too large to handle, talking to someone about such struggles or getting help to put a stop to them is crucial to prevent them for getting worse. This seeking of help usually comes in the form of calling hotlines and lifelines. These lines can get cluttered, which can worsen things in situations of life and death. For this reason along others, Comet**CRISIS** is a last-option Discord helpline that attempts to mitigate some of these situations that could lead to dangerous outcomes to the best of its ability. This hotline tries to emulate the sense of someone talking to you as you get resources.

Comet**CRISIS** itself has many topics you can receive help with, for example what you can do in case you are an LGBTQ+ member that got disowned for being who you are; to even knowing what to do if ICE (a U.S. immigration agency) is at your door steps.

Comet**CRISIS** lists hotlines to resources such as the Trevor Project and in cases of suicide prevention lists a website that contains hotlines to a country's suicide lifelines. In addition, Comet**CRISIS** lists tips to follow in a situation.

When the tips in Comet**CRISIS** aren't enough, the user can request to speak to the bot developer. If the user requests this, the bot will send an SOS Signal (a ping) to the Developer that will contain information about the situation. The urgency levels are as follows:
> **Level 1**: High Risk of Severe Injury and/or Death:
> 
> Only to be used in cases where a user can result severely injured or dead. Suicide SOS signals are automatically placed in Level 1 due to the nature of the crisis.

> **Level 2**: High Risk of Injury and Low, But Increasing Risk of Death:
> 
> Used in cases where a user can result injured and where the threat of death could increase if left unanttended. To be used in situations like lack of food/shelter and/or disownment of a LGBTQ+ person.

> **Level 3**: Medium-Low Risk of Injury. Virtually No Risk of Death:
> 
> This level is for situations where a user can result injured, but will almost likely be able to safely withstand it. To be used in situations like lack of food/shelter and/or disownment of a LGBTQ+ person that hasn't lead or will lead to the prson running for their lives.

> **Level 4**: No Risk of Injury or Death. General Questions:
> 
> This level is for situations where a user won't result injured or dead. To be used in times where a user needs to talk to someone without it being a emergency or to get information on how to deal with stressful situations.

To engage with Comet**CRISIS**, you run `#crisis`. The command will be available in English and Spanish when V3.0 `Bellatrix` launches, or by latest V4.0 `Proxima Centauri`.

### Blacklist
Slurs are a rampant problem. They may generate problems and cause unecessary problems. This thankfully counters such issue by instantly deleting a offending message without mod intervention. In addition the slur list can be customized to the needs of each server without any issue. In addition, the blacklist circumvents punctuation and translates the Unicode characters in a sentence, making the blacklist harder to bypass. To add new things to the blacklist you use `#addSlur <thing to blacklist>` and to remove an entry you do `#unslur <thing to remove>`. Note that the blacklist is indiscriminate, meaning that no role is immune and also note one server's blacklist doesnt affect another.

### Warning system
Comet's original system in the 1.0.0 Betas was based on the Replit Database library, which did not allow for the listing of reasons why a person was warned and in itself was only wired to one of the Contributor Servers. **2.0.0** changes that. Comet now not only supports a warning system whose warnings list wont affect another server's list, but one that also values transparency. When you get warned using the `#warn <member> <reason>` you receive a copy of the warning prompt that includes the moderator's name and the reason why. In addition, the `#unwarn <member> <reason>` will also to the same thing. The '#infractions <user>` command can be used to see the warnings. Finally, moderators who get warned in the system can't unwarn themselves.

### Economy Game
Comet is equipped with an economy game, where you can gain, rob, and send Chem Coins (⌬), which is the currency of the bot. You can use `#shop` to see what is available and to buy something you run `#bal <amount> <itemName>`. To begin playing, run `#bal` and the bot will make an account for you and to gain money you do `#beg`. In the economy section, users can use ⌬ to buy items that unlock commands, like `#shoot`, `#phone`, and `#solve`.

# Commands
To run a ~~cum~~command, you have to use the `#` prefix. Simple.

> #WAP

###### Charleze (charboo#0017)
Here is a list of some bot commands as of 2.0.0 __**`Aldebaran`**__:
* #char
* #wap
* #tts
* #rps
* #hangman
* #tictactoe
* #warn
* #unwarn
* ;
* #dead chat
* #dead server
* #snipe
* #SuperSnipe
* #8ball
* #topic

...along with many others!