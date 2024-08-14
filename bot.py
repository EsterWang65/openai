# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
    async def on_message_activity(self, turn_context: TurnContext):
        endpoint = "https://gjun-openai-04.openai.azure.com/"
        key = "704e7ff1aeca465aa3500124e172e2c7"
        deployment = "gpt"

        client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key = key,
        api_version="2024-05-01-preview",
        )

        completion = client.chat.completions.create(
        model=deployment,
        messages= [
        {
        "role": "user",
        "content": turn_context.activity.text
        }],
        max_tokens=800,
        )
        await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
