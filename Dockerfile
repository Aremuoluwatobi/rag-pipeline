FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Pass the token as a build argument
ARG HF_TOKEN
ENV HF_TOKEN=$HF_TOKEN

RUN python -c "
from huggingface_hub import login
import os
login(token=os.getenv('HF_TOKEN'))
from sentence_transformers import SentenceTransformer
SentenceTransformer('all-MiniLM-L6-v2')
"

EXPOSE 7860

CMD ["python", "app.py"]