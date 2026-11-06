import time
import random

from google import genai
from google.genai import errors

def generate_with_retry(
    api_key,
    prompt,
    model="gemini-2.5-flash",
    max_retries=5
):
    client = genai.Client(api_key=api_key)

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if not response.text:
                raise ValueError(
                    "Gemini returned an empty response."
                )

            return response.text

        except errors.ServerError as e:

            if attempt == max_retries - 1:
                raise

            wait_time = min(
                2 ** attempt + random.uniform(0, 1),
                30
            )

            time.sleep(wait_time)

        except errors.ClientError:
            # أخطاء مثل مفتاح غير صالح أو نموذج غير متاح
            # لا تُحل عادةً بإعادة المحاولة.
            raise

    raise RuntimeError("Generation failed.")
