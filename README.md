# Comet
## Open Source Discord.py bot to goof with
Created by Emmanuel Castillo and in collaboration with Garen Gevorgyan. Current version is 1.0.0 `Luna`

# What It Does
> It's a python bot ofc

###### Emmanuel Castillo

The Comet bot provides basic Discord Bot functionality, like a warning system and other commands to goof around with. This is all done using the __***Discord.py***__ library.

It's modular and runs 24/7 thanks to __***Flask***__ and __***Uptime Robot***__

# Features
> Comet gives other bots like Sniped! a run for its money

###### Emmanuel Castillo, *again*
As is, the bot is packed with features, such as:
* Super Snipe
* Text-to-Speech
* Revive functionality
* Blacklist
* Economy Game
* Adaptability to the warning system of Mods

### Super Snipe
Typical snipe bots only snipe one message at a time and when another message gets deleted, so does that message. This bot solves that issue because it can capture up to three deleted messages before discarding them in favor of new ones.

To use it, use the command ``#SuperSnipe``, which will default to the first deleted message. For other messages, use ``#SuperSnipe (number)`` to see them.

### Text-To-Speech
Bots like Yggdrasil offer a TTS functionality, but its capped at 45 characters or even less. Comet introduces a unlimited character TTS that not only can it be as long as the person inputs, but also supports multiple languages thanks to gTTS. In addition, the command will translate the text to the language of your choice so Comet can dictate it in that language. To use TTS you do `#tts <text>` and then an embed will appear allowing you to choose your language. Suported languages are English, Spanish, Armenian, Korean, and Tagalog (Filipino)

### Revive Functionality
Servers die. This is due to a lack of new conversations that keep people engaged in the server. Thankfully, Comet tries to fix this by giving a random question using the ``#topic`` command, which will give a random question (or statement) to start a conversation.

### Blacklist
Slurs are a rampant problem. They may generate problems and a image of a member saying a slur may get into the public, allowing them to get cancelled. This thankfully counters such issue by instantly deleting a offending message without mod intervention. In addition the slur list can be customized to the needs of each server without any issue. In addition, the blacklist circumvents punctuation in a sentence, making the blacklist harder to bypass. To add new things to the blacklist you use `#addSlur <thing to blacklist>` and to remove an entry you do `#unslur <thing to remove>`

### Economy Game
Comet is equipped with an economy game, where you can gain, rob, and send Chem Coins (⌬), which is the currency of the bot. You can use `#shop` to see what is available and to buy something you run `#bal <amount> <itemName>`. To begin playing, run `#bal` and the bot will make an account for you and to gain money you do `#beg`. 

### Adaptability to Warning Systems
Warning systems will get a boost with this bot because it counts how many times a member has broken the rules. If such member gets a warning after their "Last Chance", Comet will warn the mod team that the member has enough warning to get kicked out of their server. The number to activate this can be tweaked inside the warn function code. To warn a member, run `#warn <member> <reason>` and to see how much warnings they have you do `#infractions <member>` (`#infractions` can be ran by any person).

# Commands
To run a ~~cum~~command, you have to use the `#` prefix. Simple.

> #WAP

###### Chxrleze
Here is a list of some bot commands as of 1.0.0 __**`Luna`**__:
* #char
* #wap
* #tts
* #rps
* #hangman
* #tictactoe
* #expose
* #warn
* #dead chat
* #dead server
* #snipe
* #SuperSnipe
* #8ball
* #topic
* #dababy

...along with many others!