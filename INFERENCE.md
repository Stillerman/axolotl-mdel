## Prerequisites
1. Create HuggingFace account
    - Accept T/C for [Aurora](https://huggingface.co/aurora-m/aurora-m-v0.1)

## Create and Connect to RunPod Instance
1. Spin up Text Generation Inference container
    -  Click [this link](https://runpod.io/gsc?template=vrtapjy2bd&ref=jbhaolsm) and you will be taken to the runpod page where you will see “deploying with template TGI with Updated PEFT”.
    - Select Organization from top right drop down
    - **MAKE SURE YOU HAVE SELECTED CUDA 12.2 min version** ![cuda](./image/select_cuda.png)
    - Scroll down to previous generation GPU section and click deploy on 1xA100 80GB. Smaller cheaper GPUs will also likely work.
    - Click customize deployment
        - Update `HUGGING_FACE_HUB_TOKEN` with your read hf token from hf.co/settings/tokens
        - Update `Container Start Command` to point at your expert lora ex `--model-id stillerman/mtg-aurora`
        - Click set overrides
    - Click continue -> deploy
    - Click the logs button on the created pod. When it is done settingup you will see `WARN text_generation_router: router/src/main.rs:327: Invalid hostname, defaulting to 0.0.0.0`
    - Close the logs -> click connect -> Connect to HTTP Service [Port 80]
    - This will open in a new tab. There will be nothing on the page but this is the base url for the api.

## Inference

- On any computer you can now issue http post requests like so

```
curl https://<YOUR BASE URL>/generate \
    -X POST \
    -d '{"inputs":"Name:","parameters":{"max_new_tokens":1024, "do_sample":true, "repetition_penalty":1.1, "top_p":0.95, "top_k":40, "temperature": 0.9, "stop":["###"], "return_full_text": true}}' \
    -H 'Content-Type: application/json'

```

The parameters of inference change the quality a good amount, so they should be experimented with for each use case.