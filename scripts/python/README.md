# Python scripts

They can be divided in a couple of categories: automations, services and archive.
Automations are for the things that are supposed to make my life better.
Services is for middleware kind of things.
Archive should speak for itself, these scripts are no longer in use.

# Automations

The following automations are currently in use:

Check_updates.py: Sends the current amount of updates that are ready to be installed for two of my hosts.

Task_date_reset.py: Resets the dates of my todoist tasks to "Today" each night through a cronjob so my tasks will always be due today.

# Services

The following middleware is currently available in services:

Wrapraid.py: A wrapper for Snapraid, which also checks if there has previously been an error and then doesn't run and informs me about this.

Telegram_apprise.py: A script you can call to send Telegram messages to a specific chat via Apprise.