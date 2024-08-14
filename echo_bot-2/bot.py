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
        endpoint = "https://gjun-open-ai-01.openai.azure.com/"
        key = "06b35311df204daa9a7cb65e0cd4e65b"
        deployment = "gpt"

        client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=key,
            api_version="2024-05-01-preview",
        )

        completion = client.chat.completions.create(
            model=deployment,
            messages= [
                {
                "role": "user",
                "content": turn_context.activity.text
                }
            ],
            max_tokens=2000
        )
        await turn_context.send_activity(completion.choices[0].message.content)

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
