from flask import Flask,request,Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter,BotFrameworkAdapterSettings
import asyncio

from Botstart import EchoBot

app = Flask(__name__)
loop = asyncio.get_event_loop()
//changesmade
botadaptersettings = BotFrameworkAdapterSettings("55981b1a-6464-4190-9e62-c54406ee68bf","a439a2d3-9d6b-4d6d-86d1-4e3fc35aecbd")
botadapter = BotFrameworkAdapter(botadaptersettings)

ebot = EchoBot()

@app.route("/api/messages",methods=["POST"])
def messages():
    if "application/json" in request.headers["content-type"]:
      jsonmessage = request.json
    else:
      return Response(status=415)

    activity = Activity().deserialize(jsonmessage)

    async def turn_call(turn_context):
        await ebot.on_turn(turn_context)

    task = loop.create_task(botadapter.process_activity(activity,"",turn_call))
    loop.run_until_complete(task)
    

if __name__ == "__main__":
    try:
        app.run('localhost',3978)
    except Exception as error:
        raise error
