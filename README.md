# D2 Discord "Bot"
## Overview
This is a "bot" built to utilize AWS Lambdas and Eventbridge rules to push a message to a webhook for your Discord server.
This is not really a "bot" as it is not designed to receive any input, only to push information.

## Infrastructure
Typically bots are run off of a computer of some sort.  You start the bot and it runs indefinitely, responding to queries and whatnot.  However I did not want this running on my computer, and I for sure didn't want to pay for a cloud computer to run this.

Solution:  Lambdas

AWS Lambdas only charge based off of what you use.  For a Lambda, you have to go through a serious amount of invocations before it starts charging you.  Even when it does begin charging, it's a miniscule amount(less than a penny) per invocation.

Some pricing information below.  Please not that I am not responsbile for Lambda charges.  Follow AWS best practices when creating an account, be sure to have MFA enabled on your root account, etc.

Source: https://aws.amazon.com/lambda/pricing/

If this is something you are not comfortable with(or don't have a credit card) there are ways to utilize Powershell or Bash to loop the bot to run every hour.  That's the purpose of the "infrastructure".

## Deployment - WIP
Note that this section is *not* complete as of the current commit.  This is a handrolled AWS deployment and does not function without some AWS knowledge.

Terraform will be utilized to deploy to AWS with a step-by-step on how to do so.
