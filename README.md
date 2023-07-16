# App Store & Play Store free paid apps grabber Telegram Bot

## Description 

This script scraps a website that hosts daily refreshed paid apps on both App Store and Play Store that became free for a limited time. It then sends it through a *Telegram Bot* you create.

This script showcases how algorithms can improve the efficiency of your workload. As well as following the coding standers, such as *Code Reuse*, *DRY(Don't Repeat Yourself)*.

## Features 

1. **Friendly user interface:** You use a preferred social media to deliver your service.
2. **Fast responses:** It checks whether the last request was made in less than 12 hours, if so, it will not scrape the web once again, because it is unlikely that the free apps have changed.
3. **Filtered results:** You can choose what category you want to look for, e.g. apps, games, packs.
4. **Light code:** I have managed to shorten the functions as possible.

## Installation

1. Clone the repository
```bash
git clone https://github.com/Ho9mes/free_paid_apps_bot.git
```
2. Get into the directory

3. Install the requirements
```bash
pip install -r requirments.txt
```
4. Create your own telegram bot and **edit the script at line 7** to put your API key

5. Make sure to create the command list in the telegram bot for a better experience.

6. Run the script.

```bash
python3 free_apps.py
```
