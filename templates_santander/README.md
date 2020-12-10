# CloudFormation Stacks For Santander

> Samples CloudFormation Stack for Santander

## Overview
This directory provides a set of [AWS
CloudFormation](https://aws.amazon.com/cloudformation/) templates to
automatically build and deploy a demo site with the Lex web interface from
this project. The templates can be used to create and manage associated
resources such as the Lex Bot and Cognito Identity Pool.

## Templates:
There are 5 CloudFormation templates

* Template that deploys the UI solution and the QnA Chatbot together using Github to host the UI code. 
* Template that deploys the UI solution and the QnA Chatbot together using CodeCommit to host the UI code. 
* Template that deploys only the UI solution (github). You will need to give Input Parameter "Bot name" to be linked with the UI

    This allows to have multiple UI linked to the same Chatbot

* Template that deploys only the UI solution (codecommit). You will need to give Input Parameter "Bot name" to be linked with the UI

    This allows to have multiple UI linked to the same Chatbot
    
* Template that deploys only the QnA chatbot

## Run the Templates:

### regions

Depending on the regions, when deploying the template. Make sure you set up BoostrapBucked as follows: 

* EU-WEST-1 ->
    BootstrapBucket = aws-bigdata-blog-replica-eu-west-1
* US-EAST-1 ->
    BootstrapBucket = aws-bigdata-blog