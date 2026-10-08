import json
from datetime import datetime

LOG_FILE = "ai_logs.jsonl"


def log_prediction(
    model,
    input_data,
    prediction,
    latency
):

    record = {
        "timestamp":
            datetime.now().isoformat(),

        "model":
            model,

        "input":
            input_data,

        "prediction":
            prediction,

        "latency_ms":
            latency
    }

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            json.dumps(record)
            + "\n"
        )


log_prediction(
    "classifier-v1",
    {"text": "hello"},
    "positive",
    23
)

print("Logged.")