# Comet
## Open Source Discord.py bot to goof with
![Comet Logo](static/photoToRender/CometProfile.jpg)

Created by Emmanuel Castillo and in collaboration with Garen Gevorgyan. Current version is 2.0.0 `Aldebaran`

To see if the bot is up, check: https://cometbot.emmanuelch.repl.co

# What It Does
> It's a python bot ofc

###### Emmanuel Castillo

The Comet bot provides basic Discord Bot functionality, like a warning system and other commands to goof around with. This is all done using the __***Discord.py***__ library.

It's modular and runs 24/7 thanks to __***Flask***__ and __***Uptime Robot***__

The website is coded in HTML and CSS working together. The animations are made possible because of [animistia](https://animista.net/play).

# Features
> Comet gives other bots like Sniped! a run for its money

###### Emmanuel Castillo, *again*
As is, the bot is packed with features, such as:
* Super Snipe
* Text-to-Speech
* Revive functionality
> * #topic
> * AI Chatbot
* Blacklist
* Warning System
* Economy Game
* Edit Snipe

### Super Snipe
Typical snipe bots only snipe one message at a time and when another message gets deleted, so does that message. This bot solves that issue because it can capture up to three deleted messages before discarding them in favor of new ones.

To use it, use the command ``#SuperSnipe``, which will default to the first deleted message. For other messages, use ``#SuperSnipe (number)`` to see them.

### Text-To-Speech
Bots like Yggdrasil offer a TTS functionality, but its capped at 45 characters or even less. Comet introduces a unlimited character TTS that not only can it be as long as the person inputs, but also supports multiple languages thanks to gTTS. In addition, the command will translate the text to the language of your choice so Comet can dictate it in that language. To use TTS you do `#tts <text>` and then an embed will appear allowing you to choose your language. Suported languages are English, Spanish, Armenian, Korean, and Tagalog (Filipino)

### Revive Functionality
#### #topic
Servers die. This is due to a lack of new conversations that keep people engaged in the server. Thankfully, Comet tries to fix this by giving a random question using the ``#topic`` command, which will give a random question (or statement) to start a conversation.
#### AI Chatbot
The bot has a built-in Chat Bot due to CodeWithSwastik's and others' work on the PRSAW python library. To talk to the bot use the `:` prefix before the sentence you want to tell it.

### Blacklist
Slurs are a rampant problem. They may generate problems and a image of a member saying a slur may get into the public, allowing them to get cancelled. This thankfully counters such issue by instantly deleting a offending message without mod intervention. In addition the slur list can be customized to the needs of each server without any issue. In addition, the blacklist circumvents punctuation in a sentence, making the blacklist harder to bypass. To add new things to the blacklist you use `#addSlur <thing to blacklist>` and to remove an entry you do `#unslur <thing to remove>`. Note that the blacklist is indiscriminate, meaning that no role is immune and also note on server's blacklist doesnt affect another.

### Warning system
Comet's original system in the 1.0.0 Betas was based on the Replit Database library, which did not allow for the listing of reasons why a person was warned and in itself was only wired to one of the Contributor Servers. **2.0.0** changes that. Comet now not only supports a warning system whose warnings list wont affect another server's list, but one that also values transparency. When you get warned using the `#warn <member> <reason>` you receive a copy of the warning prompt that includes the moderator's name and the reason why. In addition, the `#unwarn <member> <reason>` will also to the same thing. The '#infractions <user>` command can be used to see the warnings. Finally, moderators who get warned in the system can't unwarn themselves.

### Economy Game
Comet is equipped with an economy game, where you can gain, rob, and send Chem Coins (⌬), which is the currency of the bot. You can use `#shop` to see what is available and to buy something you run `#bal <amount> <itemName>`. To begin playing, run `#bal` and the bot will make an account for you and to gain money you do `#beg`. 

### Edit Snipe
A message's meaning can be altered by obviously editing it. This means that if you wanted to see what the message read previously, you had to be there or download 3rd-Party addons to see it. Thankfully, Comet bypasses this by the creation of the `#edit` command, which shows you how a message was before it was edited and how it is after its edited. Multiple edit message viewing is planned for V3 by latest. Beware `#edit` has a 60-second timer to check what were the contents of the message before the command gets cleared

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
* #dababy

...along with many others!