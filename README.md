
# Decrypt Discord Bot

This project is the capstone project for Human Language Technologies (HLT). It is a discord bot that detects the personal information in the messages and masks them accordingly.




![Original Message](https://media.discordapp.net/attachments/1229828828688289802/1230126736495345725/image.png?ex=66322fcc&is=661fbacc&hm=74f0090ce8b6620512b5a6f72f9a4d51aa39a8b231a46c43d267bbee34f38ae6&=&format=webp&quality=lossless&width=694&height=96)

![masked image](https://media.discordapp.net/attachments/1229828828688289802/1230126777029103657/image.png?ex=66322fd6&is=661fbad6&hm=74f0d6e0d07b46651c02272f6ac5ac08a5fff236d558ae9986f0ff61a4b54d5b&=&format=webp&quality=lossless&width=709&height=113)

![unvailing mask](https://cdn.discordapp.com/attachments/1229828828688289802/1230126792363474974/image.png?ex=66322fd9&is=661fbad9&hm=3fabb76c33b9c80e0d3820da2e77d74abf4802c9381879f152850d99b5be8e4c&)


## Run Locally

Clone the project

```bash
  git clone https://github.com/liza1212/Discrypt.git
```

Go to the project directory

```bash
  cd Discrypt
```

Go to the implementation you want of either T5 or Mistral-7b

```bash
cd t5-bot
```
or,
```bash
cd mistral-bot-GPU
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Go to the following 
[link](https://drive.google.com/drive/folders/1-eHVGqaTMAXLzYNiCzo_OaQ22rBrjlog?usp=sharing) to get the finetuned checkpoints.

Generate your Bot Token ID if you want to build your own bot through the instructions in [Discord Developer Docs](https://discord.com/developers/docs/intro).

Put the API key in a .env file.

For the T5 model, start the bot after loading the checkpoint
```bash
cd t5-bot
python pii_bot.py
```

For Mistral, start the webapp, then start the bot
```bash
cd mistral-bot-GPU
python webapp.py
python pii_bot.py
```




## Authors

- [@liza1212](https://github.com/liza1212)
- [@PrabigyaAcharya](https://github.com/PrabigyaAcharya)
- [@shahchhatru](https://github.com/shahchhatru)
