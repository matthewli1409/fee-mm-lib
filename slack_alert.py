import os
import textwrap
from dotenv import load_dotenv
from slack import WebClient
from typing import Union

load_dotenv()

sc = WebClient(os.getenv(f'SLACK_KEY'))


class SlackIcons:
    BEAR = 'https://i.imgur.com/PMgfJSm.jpg'
    BULL = 'https://i.imgur.com/XBPqXUp.png'
    CAT = 'https://i.imgur.com/mIcObyL.jpeg'
    CHICKEN = 'https://i.imgur.com/3E7nnfl.jpg'
    COW = 'https://i.imgur.com/bl3C3TC.png'
    DOG = 'https://i.imgur.com/D38t9ai.jpg'
    ERROR = 'https://i.imgur.com/zhqaxLY.png'
    FROG_SMILE = 'https://i.imgur.com/St8whhu.gif'
    FROG_CRY = 'https://i.imgur.com/Acpk9Uv.png'
    FROG_SKELETON = 'https://i.imgur.com/IhQgU5V.jpeg'
    RADIATION = 'https://i.imgur.com/XZSIfbA.png'
    TAP = 'https://i.imgur.com/GhAQZDQ.png'


def send_generic_msg(messages: Union[list, str], title: str, icon_url: str, channel: Union[str, None] = None,
                     markdown: bool = False, attachment_path: Union[str, None] = None,
                     attachment_name: Union[str, None] = None, attachment_type: Union[str, None] = None):
    """Generic slack message template

    Args:
        messages (list of str): list of messages to send in Slack message
        title (str): appears on the title line of Slack message
        icon_url (str): url for image of bot
        channel (:str, optional): to specify a specific channel. Defaults to None.
        markdown (:bool, optional): send normal message if False, else markdown if True. Defaults to False.
        attachment_path (str): path of a file
        attachment_name (str): attachment name
        attachment_type (str): attachment type
    """
    if len(messages) == 0:
        return

    merged_messages = merge(messages, 2000)

    for message in merged_messages:
        sc.chat_postMessage(
            channel=channel,
            username=title,
            parse="full",
            icon_url=icon_url,
            blocks=[{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": message
                }
            }] if markdown else None,
            text=message if not markdown else None
        )
        if attachment_path:
            sc.files_upload(channels=channel, file=attachment_path, filetype=attachment_type,
                            filename=attachment_name)


def merge(messages, n=2000):
    """Merge messages maintain the maximum length < n"""
    merged_messages = []

    merged_message = ""
    while len(messages) > 0:
        message = messages.pop(0)

        if len(message) > n:
            # Handle critical case when one message alone is too long
            message = "\n".join(textwrap.wrap(message, n, break_long_words=False, replace_whitespace=False))

        if len(message) + len(merged_message) > n:
            # Can we merge the two messages without making the resulting message too long?
            # Case no
            merged_messages.append(merged_message)
            merged_message = message
        else:
            # Case yes
            merged_message += f"\n{message}"

    merged_messages.append(merged_message)
    return merged_messages


def send_private_message(user_id, username, messages, as_user=False, markdown=False, icon_url=SlackIcons.BULL,
                         attachment_path=None, attachment_type=None, attachment_name=None):
    conversation = sc.conversations_open(users=[user_id])
    channel_id = conversation['channel']['id']

    merged_messages = merge(messages, 2000)

    for message in merged_messages:
        sc.chat_postMessage(
            channel=channel_id,
            username=username,
            parse="full",
            icon_url=icon_url,
            text=message if not markdown else None,
            blocks=[{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": message
                }
            }] if markdown else None,
            as_user=as_user
        )
        if attachment_path:
            sc.files_upload(channels=channel_id, file=attachment_path, filetype=attachment_type,
                            filename=attachment_name)
